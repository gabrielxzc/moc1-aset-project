import { range, randomInt } from "../../commonlib/utils";
import { randomAudioTags } from "../../commonlib/audio-tags";

const MAX_NUMBER_OF_RETURNED_AUDIO_FILES = 15;

export const getAudioFiles = async tags => {
  const normalizedTags =
    typeof tags === "string" ? [tags] : tags !== undefined ? tags : [];

  const audioFiles = [];
  const numberOfReturnedAudioFiles = randomInt(
    1,
    MAX_NUMBER_OF_RETURNED_AUDIO_FILES
  );

  range(0, numberOfReturnedAudioFiles).forEach(() => {
    audioFiles.push({
      uri:
        "https://file-examples.com/wp-content/uploads/2017/11/file_example_MP3_700KB.mp3",
      tags: [
        ...normalizedTags,
        ...randomAudioTags(normalizedTags, randomInt(1, 3))
      ]
    });
  });

  return audioFiles;
};
