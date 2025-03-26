import styled from "styled-components";
import Header from "./components/Header";
import { useContext, useState } from "react";
import { ThemeContext } from "./context/themeContext";
import Body from "./components/Body";
import Output from "./components/Output";

function App() {
  const { theme } = useContext(ThemeContext);
  const [changeDetector, setChangeDetector] = useState(0);

  function addNewOutput() {
    setChangeDetector(x => x + 1);
  }

  return (
    <Wrapper theme={theme}>
      <Header />
      <Body addNewOutput={addNewOutput} />
      <Output changeDetector={changeDetector} />
    </Wrapper>
  );
}







const Wrapper = styled.div`
  background-color: ${(props) => props.theme.bgcolor};
  color: ${(props) => props.theme.color};
  box-sizing: border-box;
  max-width: 100vw;
  min-height: 100vh;
  margin: 0px;
  padding: 0px;
  position: relative;
`;

export default App;
