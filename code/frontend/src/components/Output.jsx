import React, { useContext, useEffect, useState } from 'react';
import styled from 'styled-components';
import { ThemeContext } from '../context/themeContext';

function Output({ changeDetector }) {
    const [outputs, setOutputs] = useState([]);
    const { theme } = useContext(ThemeContext);

    useEffect(() => {
        let localStorage_Outputs = JSON.parse(localStorage.getItem('genai_outputs')) || [];
        // localStorage_Outputs = localStorage_Outputs.map(x => JSON.parse(x));
        setOutputs(localStorage_Outputs);
    }, [changeDetector]);

    return (
        <Box theme={theme}>
            {/* <Grid theme={theme}>
                <GridHeader theme={theme}>Key</GridHeader>
                <GridHeader theme={theme}>Value</GridHeader>

                <GridItem theme={theme}>From</GridItem>
                <GridItem theme={theme}>ayush@gmail.com</GridItem>
            </Grid> */}

            {
                outputs.map((output, ind) => {
                    return (
                        <>
                            <h4>{output.filename}</h4>
                            <Grid key={'i' + ind} theme={theme}>
                                <GridHeader theme={theme}>Key</GridHeader>
                                <GridHeader theme={theme}>Value</GridHeader>

                                <GridItem theme={theme}>Urgency</GridItem>
                                <GridItem theme={theme}>{output.urgency}</GridItem>

                                <GridItem theme={theme}>Subject</GridItem>
                                <GridItem theme={theme}>{output.subject}</GridItem>

                                <GridItem theme={theme}>From</GridItem>
                                <GridItem theme={theme}>{output.from}</GridItem>

                                <GridItem theme={theme}>To</GridItem>
                                <GridItem theme={theme}>{output.to}</GridItem>

                                <GridItem theme={theme}>Timestamp</GridItem>
                                <GridItem theme={theme}>{output.timestamp || 'N.A.'}</GridItem>

                                <GridItem theme={theme}>Summary of Email</GridItem>
                                <GridItem theme={theme}>{output.summary}</GridItem>

                                <GridItem theme={theme}>Request Type</GridItem>
                                <GridItem theme={theme}>{output.req_type || 'N.A.'}</GridItem>

                                <GridItem theme={theme}>Sub-Request Type</GridItem>
                                <GridItem theme={theme}>{output.sub_req_type || 'N.A.'}</GridItem>

                                <GridItem theme={theme}>Confidence</GridItem>
                                <GridItem theme={theme}>{output.confidence_score * 100}</GridItem>
                                {
                                    output.overlapping_requests?.length>0 && <>
                                        <GridItem theme={theme}>Other Possible Request Types</GridItem>
                                        <GridItem theme={theme}>{output.overlapping_requests.join(', ')}</GridItem>
                                    </>
                                }
                            </Grid>
                        </>
                    );
                })
            }
        </Box>
    );
}





const Box = styled.div`
    box-sizing: border-box;
    position: relative;
    margin: 2rem 1rem;
    margin-bottom: 0px;
    width: calc(100% - 2rem);
    padding-left: 0.5rem;
    padding-right: 0.5rem;
    padding-bottom: 1rem;
    border-radius: 0.75rem;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    color: ${props => props.theme.color};

    h4 {
        text-align: center;
        width: 100%;
        margin: 0px;
    }
`;

const Grid = styled.div`
    display: grid;
    width: 100%;
    max-width: 1500px;
    margin: 0px;
    margin-bottom: 2rem;
    grid-template-columns: 1fr 4fr;
    /* row-gap: 0.5rem; */
    column-gap: 0rem;
    /* border: 2px solid ${props => props.theme.color}; */
    padding: 10px;
    div:nth-child(even) {
        border-left: 0;
    }
    div:not(:nth-last-child(-n+2)) {
        border-bottom: 0;
    }
    @media screen and (min-width: 480px) {
        width: 95%;
    }
    @media screen and (min-width: 768px) {
        width: 90%;
    }
    @media screen and (min-width: 1280px) {
        width: 80%;
    }
`;

const GridItem = styled.div`
    padding: 4px;
    border: 1px solid ${props => props.theme.color};
    text-align: center;
    border-collapse: collapse;
    border-spacing: 0px;
`;

const GridHeader = styled(GridItem)`
    font-weight: bold;
    background-color: ${props => props.theme.secondary};
`;

export default Output;