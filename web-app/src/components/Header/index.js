import React from "react";

function Header() {
  return (
    <section className="section">
      <div className="container is-centered">
        <h1 className="title has-text-centered">
          Clink{" "}
          <span className="icon is-large">
            <i className="fas fa-assistive-listening-systems" />
          </span>
        </h1>
        <p className="subtitle has-text-centered">
          Your audio tagging assistant, powered by{" "}
          <a
            href="https://www.kaggle.com/c/freesound-audio-tagging-2019"
            target="_blank"
            rel="noopener noreferrer"
          >
            Freesound Audio Tagging 2019
          </a>
        </p>
      </div>
    </section>
  );
}

export default Header;
