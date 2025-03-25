import React, { useContext, useState } from 'react';
import styled from 'styled-components';
import { ThemeContext } from '../context/themeContext';
import Loading from './Loading';

function Body() {
    const { theme } = useContext(ThemeContext);
    const [loading, setLoading] = useState(false);

    function fileSelectFn(e) {
        e.preventDefault();
        setLoading(true);
        fetch(`${import.meta.env.VITE_SERVER_URL}/`, {
            method: 'POST',
        }).then(res => {
                return res.json();
            }).then(body => {

            }).catch(err => {

            }).finally(() => {
                setLoading(false);
            });
    }
    return (
        <Box>
            <H1>Classify EML Files</H1>
            <H5>'Download Message' from Google Mail and Classify them.</H5>
            <InputBox>
                <Label htmlFor='emlinput' theme={theme}>
                    Select EML Files
                    <input onChange={fileSelectFn} type='file' accept='.eml' id='emlinput' style={{ display: 'none' }}></input>
                </Label>
            </InputBox>
            <Loading visible={loading.toString()} />
        </Box>
    );
}

const Box = styled.div`
    position: relative;
    margin: 2rem auto;
    padding-left: 0.5rem;
    padding-right: 0.5rem;
    border-radius: 1rem;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    width: 85%;
    @media screen and (min-width: 480px) {
        width: 80%;
        margin: 2rem auto;
        border: 2px solid ${props => props.theme.color};
        padding-left: 1rem;
        padding-right: 1rem;
    }
    @media screen and (min-width: 768px) {
        width: 70%;
    }
    @media screen and (min-width: 1280px) {
        width: 60%;
    }
`;

const H1 = styled.h1`
    margin-bottom: 4px;
    word-spacing: 0.05em;
`;

const H5 = styled.h5`
    margin-top: 0px;
    margin-bottom: 1rem;
    word-spacing: 0.05em;
`;

const InputBox = styled.div`
    padding: 0px;
    margin: 1rem 0px;
`;

const Label = styled.label`
    font-weight: bold;
    padding: 1rem;
    border-radius: 0.5rem;
    background-color: ${props => props.theme.primary};
    color: #fefefe;
    word-spacing: 0.05em;
    user-select: none;
    display: flex;
    word-wrap: break-word;
    cursor: pointer;
`;

export default Body;