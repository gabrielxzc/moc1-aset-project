import { post } from "../protocols/http/methods";

const tagAudioFile = async file => {
  return new Promise((resolve, reject) => {
    const reader = new FileReader();
    reader.readAsDataURL(file);

    reader.onload = async () => {
      const response = await post("http://localhost:5000/tag", {
        data: { file: reader.result }
      });

      resolve(response);
    };

    reader.onerror = err => {
      console.error(err);
      reject(err);
    };
  });
};

export default tagAudioFile;
