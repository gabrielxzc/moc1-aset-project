import React from "react";

function SearchBar() {
  return (
    <>
      <section className="section">
        <div className="columns is-centered">
          <div className="field has-addons column is-two-fifths">
            <div className="control is-expanded">
              <input
                className="input"
                type="text"
                placeholder="Add a tag, e.g Bark and search for audio files!"
              />
            </div>
            <div className="control">
              <button className="button is-info">Search</button>
            </div>
          </div>
        </div>
        <div className="columns is-centered">
          <div className="tags are-medium">
            <span className="tag is-info">
              Bass drum
              <button className="delete is-small"></button>
            </span>
            <span className="tag is-info">
              Bass guitar
              <button className="delete is-small"></button>
            </span>
            <span className="tag is-info">
              Chink and clink
              <button className="delete is-small"></button>
            </span>
            <span className="tag is-info">
              Chirp
              <button className="delete is-small"></button>
            </span>
          </div>
        </div>
      </section>
    </>
  );
}

export default SearchBar;
