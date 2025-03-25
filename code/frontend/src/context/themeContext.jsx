import React, { useState, createContext } from 'react';

const ThemeContext = createContext();

const lightTheme = {
    id: 0,
    primary: '#f44336',
    secondary: '#536DFE',
    bgcolor: '#fafafa',
    color: 'black',
    loader: {
        color: "#fafafa",
        bgcolor: "#1212122f"
    }
};

const darkTheme = {
    id: 1,
    primary: '#f44336',
    secondary: '#536DFE',
    bgcolor: '#121212',
    color: 'white',
    loader: {
        color: "#121212",
        bgcolor: "#fafafa2f"
    }
};

function ThemeState(props) {
    const [theme, setTheme] = useState(darkTheme);

    const toggleTheme = () => {
        setTheme(prevTheme => {
            if (prevTheme.id === 0) return darkTheme;
            else return lightTheme;
        });
    }

    return (
        <>
            <ThemeContext.Provider value={{ theme, toggleTheme }}>
                {props.children}
            </ThemeContext.Provider>
        </>
    );
}


export { ThemeContext, ThemeState };