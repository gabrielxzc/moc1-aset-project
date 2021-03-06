import React, { useState } from "react";
import { withRouter } from "react-router-dom";
import queryString from "query-string";

import InputWithSuggestions from "../generic/InputWithSuggestions";
import AudioTags from "../../elements/AudioTags";

import { ALL_AUDIO_TAGS } from "../../commonlib/audio-tags";

const AudioTagsInput = props => {
  const [selectedAudioTags, setSelectedAudioTags] = useState([]);

  const getSuggestedAudioTags = async tagPrefix => {
    const suggestedAudioTags = [];

    for (const audioTag of ALL_AUDIO_TAGS) {
      if (audioTag.toLowerCase().startsWith(tagPrefix.toLowerCase())) {
        suggestedAudioTags.push(audioTag);
      }
    }

    return suggestedAudioTags;
  };

  const handleAdd = audioTag => {
    setSelectedAudioTags([...selectedAudioTags, audioTag]);
  };

  const handleDelete = audioTag => {
    const newSelectedAudioTags = [...selectedAudioTags];
    newSelectedAudioTags.splice(newSelectedAudioTags.indexOf(audioTag), 1);

    setSelectedAudioTags(newSelectedAudioTags);
  };

  const handleSearch = () => {
    props.history.push({
      pathname: props.location.pathname,
      search: queryString.stringify({tags: selectedAudioTags})
    });
  };

  return (
    <section className="section">
      <div className="columns is-centered">
        <div className="field has-addons column is-two-fifths">
          <div className="control is-expanded">
            <InputWithSuggestions
              id="audio-tags-input"
              placeholder="Clapping"
              onAdd={handleAdd}
              getSuggestions={getSuggestedAudioTags}
              help={
                "Add one or multiple tags then press the search button when you are ready!"
              }
            />
          </div>
          <div className="control">
            <button className="button is-info" onClick={handleSearch}>
              Search
            </button>
          </div>
        </div>
      </div>
      <div className="columns is-centered">
        <AudioTags tags={selectedAudioTags} isWithDeleteIcon={true}
                   handleTagDelete={(tag) => handleDelete(tag)}/>
      </div>
    </section>
  );
};

export default withRouter(AudioTagsInput);
