import React from "react";
import { BrowserRouter } from "react-router-dom";

import Header from "../Header";
import TagFileArea from "../TagFileArea";
import AudioFiles from "../AudioFiles";
import AudioTagsInput from "../AudioTagsInput";

function App() {
  return (
    <BrowserRouter>
      <Header />
      <TagFileArea />
      <AudioTagsInput />
      <AudioFiles />
    </BrowserRouter>
  );
}

export default App;
