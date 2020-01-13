import axios from "axios";

const sendHttpRequest = axios.create();

const httpRequest = request => {
  return new Promise((resolve, reject) => {
    sendHttpRequest(request)
      .then(response => {
        resolve(response);
      })
      .catch(error => {
        if (error.response) {
          resolve(error.response);
        } else {
          reject(error);
        }
      });
  });
};

export default httpRequest;
