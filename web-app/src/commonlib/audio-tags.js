import { range, randomInt } from "./utils";

export const ALL_AUDIO_TAGS = [
  "Accelerating_and_revving_and_vroom",
  "Accordion",
  "Acoustic_guitar",
  "Applause",
  "Bark",
  "Bass_drum",
  "Bass_guitar",
  "Bathtub_(filling_or_washing)",
  "Bicycle_bell",
  "Burping_and_eructation",
  "Bus",
  "Buzz",
  "Car_passing_by",
  "Cheering",
  "Chewing_and_mastication",
  "Child_speech_and_kid_speaking",
  "Chink_and_clink",
  "Chirp_and_tweet",
  "Church_bell",
  "Clapping",
  "Computer_keyboard",
  "Crackle",
  "Cricket",
  "Crowd",
  "Cupboard_open_or_close",
  "Cutlery_and_silverware",
  "Dishes_and_pots_and_pans",
  "Drawer_open_or_close",
  "Drip",
  "Electric_guitar",
  "Fart",
  "Female_singing",
  "Female_speech_and_woman_speaking",
  "Fill_(with_liquid)",
  "Finger_snapping",
  "Frying_(food)",
  "Gasp",
  "Glockenspiel",
  "Gong",
  "Gurgling",
  "Harmonica",
  "Hi-hat",
  "Hiss",
  "Keys_jangling",
  "Knock",
  "Male_singing",
  "Male_speech_and_man_speaking",
  "Marimba_and_xylophone",
  "Mechanical_fan",
  "Meow",
  "Microwave_oven",
  "Motorcycle",
  "Printer",
  "Purr",
  "Race_car_and_auto_racing",
  "Raindrop",
  "Run",
  "Scissors",
  "Screaming",
  "Shatter",
  "Sigh",
  "Sink_(filling_or_washing)",
  "Skateboard",
  "Slam",
  "Sneeze",
  "Squeak",
  "Stream",
  "Strum",
  "Tap",
  "Tick-tock",
  "Toilet_flush",
  "Traffic_noise_and_roadway_noise",
  "Trickle_and_dribble",
  "Walk_and_footsteps",
  "Water_tap_and_faucet",
  "Waves_and_surf",
  "Whispering",
  "Writing",
  "Yell",
  "Zipper_(clothing)"
];

export const randomAudioTags = (excludedTags, numberOfRandomTags) => {
  const tags = [];

  range(0, numberOfRandomTags).forEach(() => {
    let tag;

    while (true) {
      tag = ALL_AUDIO_TAGS[randomInt(0, ALL_AUDIO_TAGS.length - 1)];

      for (const excludedTag of excludedTags.concat(tags)) {
        if (excludedTag === tag) {
          continue;
        }
      }

      break;
    }

    tags.push(tag);
  });

  return tags;
};
