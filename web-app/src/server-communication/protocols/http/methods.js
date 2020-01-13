import httpRequest from "./request";

const httpMethod = async (method, url, optional) => {
  const { data } = await httpRequest({
    method,
    url,
    ...optional
  });

  return data;
};

export const get = async (url, optional) => {
  return await httpMethod("GET", url, optional);
};

export const post = async (url, optional) => {
  return await httpMethod("POST", url, optional);
};
