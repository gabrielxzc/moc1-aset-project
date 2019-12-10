import React from "react";

const Input = props => {
  const {
    isExpanded,
    isFocused,
    help,
    error: errorMessage,
    labelContent,
    className,
    ...inputProps
  } = props;

  const getClassNames = () => {
    let classes = "control is-relative";

    if (isExpanded) {
      classes += " is-expanded";
    }

    if (className) {
      classes += ` ${className}`;
    }

    return classes;
  };

  return (
    <>
      {labelContent && <label className="label">{labelContent}</label>}

      <div className={getClassNames()}>
        <input
          className={`input ${isFocused ? "is-focused" : ""} ${
            errorMessage ? "is-danger" : ""
          }`}
          {...inputProps}
        />

        {help && <p className="help has-text-centered">{help}</p>}
        {errorMessage && <p className="help is-danger">{errorMessage}</p>}
      </div>
    </>
  );
};

export default Input;
