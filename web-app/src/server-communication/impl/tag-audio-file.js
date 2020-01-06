import { randomAudioTags } from "../../commonlib/audio-tags";
import { randomInt, sleep } from "../../commonlib/utils";

const tagAudioFile = async file => {
  await sleep(2000);
  return randomAudioTags([], randomInt(1, 3));
};

export default tagAudioFile;
