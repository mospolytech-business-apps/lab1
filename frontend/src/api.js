import { BACKEND_URL } from "./config";

const headers = {
  "Content-Type": "application/json",
};

export const login = ({ username, password }) =>
  fetch(`${BACKEND_URL}/auth/login/`, {
    method: "POST",
    headers: { ...headers },
    body: JSON.stringify({ email: username, password }),
  }).then((res) => res.json());

export const me = ({ token }) =>
  fetch(`${BACKEND_URL}/auth/me/`, {
    method: "GET",
    headers: { ...headers, Authorization: `Bearer ${token}` },
  }).then((res) => res.json());

export const getUser = ({ id, token }) =>
  fetch(`${BACKEND_URL}/auth/user/${id}`, {
    method: "GET",
    headers: { ...headers, Authorization: `Bearer ${token}` },
  }).then((res) => res.json());

export const editUser = ({ token, email, ...props }) =>
  fetch(`${BACKEND_URL}/auth/edit/`, {
    method: "PATCH",
    headers: {
      ...headers,
      Authorization: `Bearer ${token}`,
    },
    body: JSON.stringify({ email, ...props }),
  }).then((res) => res.json());

export const getAllUsers = ({ token }) =>
  fetch(`${BACKEND_URL}/auth/users/`, {
    method: "GET",
    headers: { ...headers, Authorization: `Bearer ${token}` },
  }).then((res) => res.json());

export const offices = ({ token }) =>
  fetch(`${BACKEND_URL}/office/`, {
    method: "GET",
    headers: { ...headers, Authorization: `Bearer ${token}` },
  }).then((res) => res.json());

export const logout = ({ token, error }) =>
  fetch(`${BACKEND_URL}/auth/logout/`, {
    method: "POST",
    headers: {
      ...headers,
      Authorization: `Bearer ${token}`,
    },
    body: JSON.stringify({ error }),
  }).then((res) => res.json());

export const surveys = ({ token }) =>
  fetch(`${BACKEND_URL}/survey/`, {
    method: "GET",
    headers: { ...headers, Authorization: `Bearer ${token}` },
  }).then((res) => res.json());

export const schedules = ({ token }) =>
  fetch(`${BACKEND_URL}/schedules/`, {
    method: "GET",
    headers: { ...headers, Authorization: `Bearer ${token}` },
  }).then((res) => res.json());

export const airports = ({ token }) =>
  fetch(`${BACKEND_URL}/airport/`, {
    method: "GET",
    headers: { ...headers, Authorization: `Bearer ${token}` },
  }).then((res) => res.json());

export const cancelSchedule = ({ token, id }) =>
  fetch(`${BACKEND_URL}/schedules/${id}/`, {
    method: "PATCH",
    headers: {
      ...headers,
      Authorization: `Bearer ${token}`,
    },
    body: JSON.stringify({ Confirmed: false }),
  }).then((res) => res.json());

export const updateSchedule = ({ token, id, Date, Time, EconomyPrice }) =>
  fetch(`${BACKEND_URL}/schedules/${id}/`, {
    method: "PATCH",
    headers: {
      ...headers,
      Authorization: `Bearer ${token}`,
    },
    body: JSON.stringify({ Date, Time, EconomyPrice }),
  }).then((res) => res.json());

export const importSchedules = ({ token, formData }) =>
  fetch(`${BACKEND_URL}/schedules/import/`, {
    method: "POST",
    headers: {
      ...headers,
      Authorization: `Bearer ${token}`,
    },
    body: formData,
  }).then((res) => res.json());
