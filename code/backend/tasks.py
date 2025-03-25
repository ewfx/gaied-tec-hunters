from crewai import Task
from textwrap import dedent
import json

#the template to be filled
template = {
      "timestamp": "",
      "subject": "",
      "to": "",
      "from": "",
      "req_type": "",
      "sub_req_type": "",
      "summary_of_the_mail": "",
      "confidence_score": 0.0,
      "overlap": 0.0,
      "overlapping_requests": [],
      "duplicate": "True/False"
}

json_template = json.dumps(template)

"""
Creating Tasks Cheat Sheet:
- Begin with the end in mind. Identify the specific outcome your tasks are aiming to achieve.
- Break down the outcome into actionable tasks, assigning each task to the appropriate agent.
- Ensure tasks are descriptive, providing clear instructions and expected deliverables.

Goal:
- Develop a detailed itinerary, including city selection, attractions, and practical travel advice.

Key Steps for Task Creation:
1. Identify the Desired Outcome: Define what success looks like for your project.
    - Generate a feature and a step definition file

2. Task Breakdown: Divide the goal into smaller, manageable tasks that agents can execute.
    - feature file generation
    - step definition generation

3. Assign Tasks to Agents: Match tasks with agents based on their roles and expertise.

4. Task Description Template:
  - Use this template as a guide to define each task in your CrewAI application. 
  - This template helps ensure that each task is clearly defined, actionable, and aligned with the specific goals of your project.

  Template:
  ---------
  def [task_name](self, agent, [parameters]):
      return Task(description=dedent(f'''
      **Task**: [Provide a concise name or summary of the task.]
      **Description**: [Detailed description of what the agent is expected to do, including actionable steps and expected outcomes. This should be clear and direct, outlining the specific actions required to complete the task.]

      **Parameters**: 
      - [Parameter 1]: [Description]
      - [Parameter 2]: [Description]
      ... [Add more parameters as needed.]

      **Note**: [Optional section for incentives or encouragement for high-quality work. This can include tips, additional context, or motivations to encourage agents to deliver their best work.]

      '''), agent=agent)

"""


def save_to_file(self, filename, content):
    with open(filename, 'a') as file:
        file.write(content + '\n')

class TestTasks:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"


    def extract_details(self, agent, email_content):
        return Task(
            description=dedent(f"""
            
                **Description**: [You will be provided with the contents of a email including the subject, body and 
                the contents of the attachments.]
                
                **Task**: [You have to go through all the content of the email thouroughly and extract all the relevant information to fill the 
                json template which is provided: {json_template}]
                
                Summary of the mail should contain nested json of all the key value pairs provided in the mail along with a 
                text summary of the whole mail
                
                The request and the corresponding subrequest types in the json templates should be one of the following table and:
                
                Request type                        Subrequest Type
                AU Transfer                         ""
                Adjustment                          ""
                Closing Notice                      Relocation Fees, Amendment Fees, Reallocation Principle
                Commitment Change                   Cashless Roll, Decrease, Increase
                Fee Payment                         Ongoing Fee, Letter of Credit Fee
                Money Movement-Inbound              Principal, Interest, Principal + Interest, Principal+Interest+Fee
                Money Movement-Outbound             Timebound, Foreign Currency
                Loan Servicing                      Prepayment, Refinancing
                Account Maintainence                Freeze Request, Ownership change
                
                In the json template provided, confidence score is the accuracy by which you are detecting the request and sub
                request types.
                
                You can use this filled json as reference(do not these values as they are dummy values) which you 
                can you to create the final json:
                {
                  "timestamp": "2025-03-25T14:30:00Z",
                  "subject": "Loan Repayment Inquiry",
                  "to": "support@bankxyz.com",
                  "from": "customer123@email.com",
                  "req_type": "Loan Repayment",
                  "sub_req_type": "Early Payment",
                  "summary": "The customer wants to inquire about making an early loan repayment and any associated penalties.",
                  "confidence_score": 0.92,
                  "overlap": 0.08,
                  "overlapping_requests": ["Loan Prepayment Charges", "Loan Closure Request"],
                  "duplicate":false
                }
                
                **Parameters**: {email_content}
                                    """),



            agent=agent,
            expected_output="json_output",
            outputs=['json_output']
        )















# class TestTasks:
#     def __tip_section(self):
#         return "If you do your BEST WORK, I'll give you a $10,000 commission!"

    # def generate_feature(self, agent, api_doc, acceptance_criteria):
    #     return Task(
    #         description=dedent(f"""
    #         **Task**: [Generate the content of feature file ]
    #         **Description**: [Generate the content of feature file of java maven project to run a cucumber test case for the given
    #         acceptance criteria]
    #
    #         **Parameters**:
    #         - api documentation: {api_doc}
    #         - acceptance criteria : {acceptance_criteria}
    #         ... [Add more parameters as needed.]
    #
    #         **Note**: {self.__tip_section()}
    #         """
    #                            ),
    #         agent=agent,
    #         outputs=['feature_file_content'],
    #     )
    #
    # def generate_stepdefinitions(self, agent, api, api_doc, feature_file_content):
    #     return Task(
    #         description=dedent(f"""
    #         **Task**: [Generate the content of step definition file named "Products.java" according to given feature_file_content of java maven project]
    #         **Description**: [Generate the content of stepdefinitionsfile "Products.java" of java maven project to run a cucumber test case for the given
    #         acceptance criteria and first line use it as package stepdefinitions; ]
    #
    #         **Parameters**:
    #         - api : {api}
    #         - api documentation: {api_doc}
    #         - feature_file_content:{feature_file_content}
    #
    #
    #         **Note**: {self.__tip_section()}
    #         """
    #                            ),
    #         agent=agent,
    #         context=feature_file_content,
    #         outputs=['stepdefinition_file_content'],
    #     )
    #
    # def generate_pox_xml(self, agent, stepdefinition_file_content):
    #     return Task(
    #         description=dedent(f"""
    #         **Task**: [Generate the content of pom.xml file named "pom.xml" according to given step definition file conten of java maven project]
    #         **Description**: [Generate the content of pom.xml file when the respective stepdefinition java file is given ]
    #
    #         **Parameters**:
    #         - stepdefinitions_file_content:{stepdefinition_file_content}
    #
    #
    #         **Note**: {self.__tip_section()}
    #         """
    #                            ),
    #         agent=agent,
    #         context=stepdefinition_file_content,
    #         outputs=['pom_xml_file_content'],
    #         expected_output="""
    #         <project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    #             xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    #             <modelVersion>4.0.0</modelVersion>
    #
    #             <groupId>com.example</groupId>
    #             <artifactId>cucumber-bdd</artifactId>
    #             <version>1.0-SNAPSHOT</version>
    #
    #             <properties>
    #                 <maven.compiler.source>1.8</maven.compiler.source>
    #                 <maven.compiler.target>1.8</maven.compiler.target>
    #                 <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    #             </properties>
    #
    #             <dependencies>
    #                 <!-- Cucumber dependencies -->
    #                 <dependency>
    #                     <groupId>io.cucumber</groupId>
    #                     <artifactId>cucumber-java</artifactId>
    #                     <version>6.10.4</version>
    #                     <scope>test</scope>
    #                 </dependency>
    #                 <dependency>
    #                     <groupId>io.cucumber</groupId>
    #                     <artifactId>cucumber-junit</artifactId>
    #                     <version>6.10.4</version>
    #                     <scope>test</scope>
    #                 </dependency>
    #
    #                 <!-- JUnit dependency -->
    #                 <dependency>
    #                     <groupId>junit</groupId>
    #                     <artifactId>junit</artifactId>
    #                     <version>4.13.2</version>
    #                     <scope>test</scope>
    #                 </dependency>
    #
    #                 <!-- RestAssured dependency -->
    #                 <dependency>
    #                     <groupId>io.rest-assured</groupId>
    #                     <artifactId>rest-assured</artifactId>
    #                     <version>4.4.0</version>
    #                     <scope>test</scope>
    #                 </dependency>
    #             </dependencies>
    #
    #             <build>
    #                 <plugins>
    #                     <plugin>
    #                         <groupId>org.apache.maven.plugins</groupId>
    #                         <artifactId>maven-compiler-plugin</artifactId>
    #                         <version>3.8.1</version>
    #                         <configuration>
    #                             <source>1.8</source>
    #                             <target>1.8</target>
    #                         </configuration>
    #                     </plugin>
    #                     <plugin>
    #                         <groupId>org.apache.maven.plugins</groupId>
    #                         <artifactId>maven-surefire-plugin</artifactId>
    #                         <version>2.22.2</version>
    #                         <configuration>
    #                             <includes>
    #                                 <include>**/RunCucumberTest.java</include>
    #                             </includes>
    #                         </configuration>
    #                     </plugin>
    #                 </plugins>
    #             </build>
    #         </project>
    #         """,
    #     )
    #
    # '''def error_check(self,agent,feature_file_content,stepdefinition_file_content):
    #     return Task(
    #         description=dedent(f"""
    #         **Task**: [Generate the content of new stepdefinition file according to given feature file in case there is any error]
    #
    #         **Parameters**:
    #         - feature_file_content:{feature_file_content}
    #         - stepdefinitions_file_content:{stepdefinition_file_content}
    #
    #
    #         **Note**: {self.__tip_section()}
    #         """
    #         ),
    #         agent=agent,
    #         outputs=['new_stepdefinition_file_content'],
    #      )'''



