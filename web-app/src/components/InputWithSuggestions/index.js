import React from "react";

import Input from "../../elements/Input";
import Suggestions from "../../elements/Suggestions";

class InputWithSuggestions extends React.Component {
  constructor(props) {
    super(props);

    this.timeoutId = undefined;

    this.state = {
      suggestions: [],
      value: ""
    };
  }

  handleAdd = value => {
    this.props.onAdd(value);

    this.setState({ value: "", suggestions: [] });
    clearTimeout(this.timeoutId);
  };

  componentDidMount() {
    const inputEl = document.getElementById(this.props.id);
    inputEl.addEventListener("keydown", this.handleEnterPressed);
  }

  componentWillUnmount() {
    const inputEl = document.getElementById(this.props.id);
    inputEl.removeEventListener("keydown", this.handleEnterPressed);
  }

  handleChange = event => {
    clearTimeout(this.timeoutId);

    const { value: newValue } = event.target;
    this.setState({ value: newValue, suggestions: [] });

    if (newValue) {
      const timeoutId = setTimeout(async () => {
        const newSuggestions = await this.props.getSuggestions(newValue);

        if (this.timeoutId === timeoutId) {
          this.setState({ suggestions: newSuggestions });
        }
      }, 50);

      this.timeoutId = timeoutId;
    }
  };

  render() {
    const { props, state } = this;
    const { onChange, onAdd, getSuggestions, ...inputProps } = props;

    return (
      <div className="is-relative">
        <Input
          type="text"
          value={state.value}
          onChange={this.handleChange}
          {...inputProps}
        />
        <Suggestions
          suggestions={state.suggestions}
          onSelection={this.handleAdd}
        />
      </div>
    );
  }
}

export default InputWithSuggestions;
