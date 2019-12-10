import React from "react";
import { BrowserRouter } from "react-router-dom";

import Header from "../Header";
import UploadArea from "../UploadArea";
import AudioFiles from "../AudioFiles";
import AudioTagsInput from "../AudioTagsInput";

function App() {
  return (
    <BrowserRouter>
      <Header />
      <UploadArea />
      <AudioTagsInput />
      <AudioFiles />
    </BrowserRouter>
  );
}

export default App;
