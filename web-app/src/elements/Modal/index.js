import React, { useRef, useEffect } from "react";

const Index = (props) => {
    const modalRef = useRef(null);

    const handleClickOutside = (event) => {
        if (modalRef.current && event.target instanceof Node && !modalRef.current.contains(event.target)) {
            props.onModalClose();
        }
    };

    useEffect(() => {
        document.addEventListener("mousedown", handleClickOutside);
        return () => document.removeEventListener("mousedown", handleClickOutside);
    });

    return (
        <div className={`modal${props.isActive ? " is-active" : ""}`}>
            <div className="modal-background" />
            <div className="modal-card" ref={modalRef}>
                <header className="modal-card-head">
                    <p className="modal-card-title">{props.title}</p>
                    <button className="delete" aria-label="close" onClick={props.onModalClose} />
                </header>
                <section className="modal-card-body">{props.children}</section>
                {props.footer && <footer className="modal-card-foot">{props.footer}</footer>}
            </div>
        </div>
    );
};

export default Index;
