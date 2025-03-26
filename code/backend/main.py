import os
from crewai import Crew,Process
from textwrap import dedent
from agents import TestAgents
from tasks import TestTasks
# from langchain_google_genai import ChatGoogleGenerativeAI
from crewai import LLM
from flask import Flask, request, jsonify

import argparse
from email import policy
from email.parser import BytesParser
from PyPDF2 import PdfReader
from io import BytesIO
import docx2txt
import textract
from flask_cors import CORS
from langchain_groq import ChatGroq

app = Flask(__name__)
CORS(app)

from dotenv import load_dotenv
load_dotenv()

def save_to_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

def remove_first_and_last_line(input_file_path, output_file_path):
    with open(input_file_path, 'r') as file:
        lines = file.readlines()
    # Remove the first and last lines
    if len(lines) > 2:
        lines = lines[1:-1]
    else:
        # If the file has less than or equal to two lines, the result will be an empty list
        lines = []
    with open(output_file_path, 'w') as file:
        file.writelines(lines)

def extract_text_from_attachment(part, content_type):
    text = ""
    try:
        attachment_data = part.get_payload(decode=True)
        if content_type == "application/pdf":
            pdf_reader = PdfReader(BytesIO(attachment_data))
            for page in pdf_reader.pages:
                text += page.extract_text() + "\n"
        elif content_type in ["application/msword",
                              "application/vnd.openxmlformats-officedocument.wordprocessingml.document"]:
            text = docx2txt.process(BytesIO(
                attachment_data)) if content_type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document" else textract.process(
                BytesIO(attachment_data)).decode("utf-8")
    except Exception as e:
        text = f"Error extracting text from attachment: {str(e)}"
    return text


def save_email_content(file_stream):
    email_content = file_stream.read()
    msg = BytesParser(policy=policy.default).parse(BytesIO(email_content))


    # Extract message ID to create a unique folder
    # message_id = msg.get("Message-ID", "unknown_message").strip("<>")
    output_dir = os.path.join("",os.getcwd())
    os.makedirs(output_dir, exist_ok=True)

    # Extract required headers and body
    headers = {
        "From": msg.get("From", ""),
        "To": msg.get("To", ""),
        "Subject": msg.get("Subject", "")
    }
    body = ""
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == "text/plain":
                body = part.get_payload(decode=True).decode(errors='ignore')
                break
    else:
        body = msg.get_payload(decode=True).decode(errors='ignore')

    # Save extracted headers and body as a text file
    email_text_path = os.path.join(output_dir, "email_content.txt")
    with open(email_text_path, "w", encoding="utf-8") as f:
        f.write(f"From: {headers['From']}\n")
        f.write(f"To: {headers['To']}\n")
        f.write(f"Subject: {headers['Subject']}\n\n")
        f.write(f"Body:\n{body}\n\n")
    print(f"Email content saved to {email_text_path}")

    # Extract attachments without saving files
    attachment_count = 0
    with open(email_text_path, "a", encoding="utf-8") as f:
        for part in msg.walk():
            if part.get_content_maintype() != "multipart" and part.get_filename():
                attachment_count += 1
                filename = part.get_filename()
                content_type = part.get_content_type()

                # Write attachment details in structured format
                f.write(f"Attachment {attachment_count}\n")
                f.write(f"Type: {content_type}\n\n")

                # Extract text from supported attachments
                extracted_text = extract_text_from_attachment(part, content_type)
                if extracted_text:
                    f.write(f"{extracted_text}\n\n")



# print("## Welcome to Crew AI Template")
# print("-------------------------------")
# api = input(dedent("""Enter the base url of the api that needed to be tested   """))
# api_doc = input(dedent("""Enter the documentation of the above api's representing all end points clearly   """))
# acceptance_criteria= input(dedent("""Enter the test case to test clearly in plain english   """))


# genai = ChatGoogleGenerativeAI(model="gemini-1.5-flash",
#                            verbose=True,
#                            temperature=0.5,
#                            google_api_key=os.getenv("GOOGLE_API_KEY"))

#Declaring the llm
# os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')
# os.environ['SAMBANOVA_API_KEY']
# model = "sambanova/DeepSeek-R1-Distill-Llama-70B"
llm = LLM(
    model="sambanova/DeepSeek-R1-Distill-Llama-70B",
    # base_url=os.getenv("SAMBANOVA_BASE_URL"),

    # api_key=os.getenv("SAMBANOVA_API_KEY"),
    temperature=0.7,
    # api_key=os.getenv('SAMBANOVA_API_KEY')
)

# llm = LLM(
#     model="groq/llama-3.1-70b-versatile",
#           api_key=os.getenv("GROQ_API_KEY")
# )

# llm = ChatGroq(model_name="llama-3.1-70b-versatile")

#declaring the agents
agents = TestAgents()
tasks = TestTasks()


@app.route('/extract', methods=['GET', 'POST'])
def extract1():
    # if "file" not in request.files:
    #     return jsonify({"error": "No file provided"}), 400

    print(request.values)
    json_outputs_list = []
    print(request.files)
    print(len(request.files))
    # print(request.files["file"][0])
    for i in range(len(request.files)):
        file = request.files[f"file{i+1}"]

        # file = request.files["file"]
        print(file.filename)
        if file.filename == "":
            return jsonify({"error": "Empty filename"}), 400

        save_email_content(file.stream)
        # return jsonify({"message": "EML file processed successfully"})


        with open('email_content.txt', 'r', encoding='utf-8') as f:
            email_body = f.read()

        # setting up the agent
        email_reader_agent = agents.email_data_extractor()

        #setting up the task
        extract_email_info = tasks.extract_details(
            email_reader_agent,
            email_body
        )

        crew = Crew(
                    agents=[email_reader_agent],
                    tasks=[extract_email_info],
        )

        json_output = crew.kickoff()
        json_outputs_list.append(json_output)

    return jsonify(str(json_outputs_list))

























if __name__ == '__main__':
    app.run(host='0.0.0.0')




# #setting up the agents
# feature_agent= agents.feature_generator()
# stepdefinition_agent = agents.step_def_generator()
# pom_file_agent=agents.pom_file_generator()
# #error_agent=agents.QA_engineer()
# #setting up the tasks
# generate_feature= tasks.generate_feature(
#             feature_agent,
#             api_doc,
#             acceptance_criteria,
#         )
#
# generate_stepdefinitions = tasks.generate_stepdefinitions(
#             stepdefinition_agent,
#             api,
#             api_doc,
#             [generate_feature],
#         )
#
# generate_pox_xml = tasks.generate_pox_xml(
#             pom_file_agent,
#             [generate_stepdefinitions],
#         )
# #setting up the crew
# crew1 = Crew(
#             agents=[feature_agent],
#             tasks=[generate_feature],
#             verbose=True,
#             process=Process.sequential,
#             manager_llm=genai,
#         )
#
# crew2 = Crew(
#             agents=[stepdefinition_agent],
#             tasks=[generate_stepdefinitions],
#             verbose=True,
#             manager_llm=genai,
#         )
#
# crew3 = Crew(
#             agents=[pom_file_agent],
#             tasks=[generate_pox_xml],
#             verbose=True,
#             manager_llm=genai,
#         )
#
# feature_file_content=crew1.kickoff()
# save_to_file("java-app/src/test/resources/features/create_item.feature",feature_file_content)
# remove_first_and_last_line("java-app/src/test/resources/features/create_item.feature","java-app/src/test/resources/features/create_item.feature")
#
#
# stepdefinition_file_content=crew2.kickoff()
# save_to_file("java-app/src/test/java/stepdefinitions/Products.java",stepdefinition_file_content)
# remove_first_and_last_line("java-app/src/test/java/stepdefinitions/Products.java", "java-app/src/test/java/stepdefinitions/Products.java")
#
#
# pom_xml_file_content=crew3.kickoff()
# save_to_file("java-app/pom.xml",pom_xml_file_content)
# remove_first_and_last_line("java-app/pom.xml", "java-app/pom.xml")
#
#
# print("crew process complete and results are generated  .....")