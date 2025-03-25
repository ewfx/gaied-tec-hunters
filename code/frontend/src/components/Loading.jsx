import React, { useContext } from 'react';
import styled from 'styled-components';
import { ThemeContext } from '../context/themeContext';

function Loading({ visible }) {
    const { theme } = useContext(ThemeContext);

    return (
        <Div visible={visible} theme={theme}>
            <div className="loader"></div>
        </Div>
    );
}

const Div = styled.div`
    display: ${props => {     
        // The below usage gives warning because we're not using transient props.
        return (props.visible == 'true') ? 'flex' : 'none';
    }};
    position: absolute;
    z-index: 50;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    align-items: center;
    justify-content: center;
    background-color: ${props => props.theme.loader.bgcolor};
    color: ${props => props.theme.loader.color};
    border-radius: 1rem;
    cursor: progress;

    .loader {
        width: 50px;
        aspect-ratio: 1;
        border-radius: 50%;
        background: radial-gradient(farthest-side,${props => props.theme.secondary} 94%,#0000) top/8px 8px no-repeat,
            conic-gradient(#0000 30%,${props => props.theme.secondary});
        -webkit-mask: radial-gradient(farthest-side,#0000 calc(100% - 8px),#000 0);
        animation: l13 1s infinite linear;
    }
    @keyframes l13 { 
        100% {
            transform: rotate(1turn)
        }
    }
`;

export default Loading;