import { BACKEND_URL } from "./config";

const headers = {
  "Content-Type": "application/json",
};

export const api = {
  //auth
  login: async ({ username, password }) => {
    try {
      const response = await fetch(`${BACKEND_URL}/auth/login/`, {
        method: "POST",
        headers: { ...headers },
        body: JSON.stringify({ email: username, password }),
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(`☠️ ${data.error} (${response.status}) `);
      }

      return { res: data, err: null };
    } catch (error) {
      return { res: null, err: error };
    }
  },

  logout: async ({ accessToken }) => {
    try {
      const response = await fetch(`${BACKEND_URL}/auth/logout/`, {
        method: "POST",
        headers: {
          ...headers,
          Authorization: `Bearer ${accessToken}`,
        },
      });

      if (!response.ok) {
        throw new Error(`${response.status}`);
      }

      const data = await response.json();

      return { res: data, err: null };
    } catch (error) {
      return { res: null, err: error };
    }
  },

  // users
  getAllUsers: async ({ accessToken }) => {
    try {
      const response = await fetch(`${BACKEND_URL}/users/`, {
        method: "GET",
        headers: { ...headers, Authorization: `Bearer ${accessToken}` },
      });

      if (!response.ok) {
        throw new Error(`(${response.status}) Error requesting all users`);
      }

      const data = await response.json();

      return { res: data, err: null };
    } catch (error) {
      return { res: null, err: error };
    }
  },

  getUser: async ({ accessToken, id }) => {
    try {
      const response = await fetch(`${BACKEND_URL}/users/${id}/`, {
        method: "GET",
        headers: { ...headers, Authorization: `Bearer ${accessToken}` },
      });

      if (!response.ok) {
        throw new Error(
          `(${response.status}) Error requesting the user with id ${id}`
        );
      }

      const data = await response.json();

      return { res: data, err: null };
    } catch (error) {
      return { res: null, err: error };
    }
  },

  addUser: async ({ accessToken, ...props }) => {
    try {
      const response = await fetch(`${BACKEND_URL}/users/add/`, {
        method: "POST",
        headers: {
          ...headers,
          Authorization: `Bearer ${accessToken}`,
        },
        body: JSON.stringify(props),
      });

      if (!response.ok) {
        throw new Error(`(${response.status}) Error adding the user`);
      }

      const data = await response.json();

      return { res: data, err: null };
    } catch (error) {
      return { res: null, err: error };
    }
  },

  editUser: async ({ accessToken, id, ...props }) => {
    try {
      const response = await fetch(`${BACKEND_URL}/users/edit/${id}/`, {
        method: "PATCH",
        headers: {
          ...headers,
          Authorization: `Bearer ${accessToken}`,
        },
        body: JSON.stringify(props[0]),
      });

      if (!response.ok) {
        throw new Error(`(${response.status}) Error updating the user`);
      }

      const data = await response.json();

      return { res: data, err: null };
    } catch (error) {
      return { res: null, err: error };
    }
  },

  banUser: async ({ accessToken, id }) => {
    try {
      const response = await fetch(`${BACKEND_URL}/users/ban/${id}/`, {
        method: "PUT",
        headers: {
          ...headers,
          Authorization: `Bearer ${accessToken}`,
        },
      });

      if (!response.ok) {
        throw new Error(`(${response.status}) Error banning the user`);
      }

      const data = await response.json();

      return { res: data, err: null };
    } catch (error) {
      console.log(error);
      return { res: null, err: error };
    }
  },

  unbanUser: async ({ accessToken, id }) => {
    try {
      const response = await fetch(`${BACKEND_URL}/users/unban/${id}/`, {
        method: "PUT",
        headers: {
          ...headers,
          Authorization: `Bearer ${accessToken}`,
        },
      });

      if (!response.ok) {
        throw new Error(`(${response.status}) Error unbanning the user`);
      }

      const data = await response.json();

      return { res: data, err: null };
    } catch (error) {
      console.log(error);
      return { res: null, err: error };
    }
  },

  // offices
  getAllOffices: async () => {
    try {
      const response = await fetch(`${BACKEND_URL}/offices/`, {
        method: "GET",
        headers: { ...headers },
      });

      if (!response.ok) {
        throw new Error(`${response.status}`);
      }

      const data = await response.json();

      return { res: data, err: null };
    } catch (error) {
      return { res: null, err: error };
    }
  },

  // report
  report: async ({ accessToken }) => {
    try {
      const response = await fetch(`${BACKEND_URL}/report/`, {
        method: "GET",
        headers: { ...headers, Authorization: `Bearer ${accessToken}` },
      });

      if (!response.ok) {
        throw new Error(`${response.status}`);
      }

      const data = await response.json();

      return { res: data, err: null };
    } catch (error) {
      return { res: null, err: error };
    }
  },

  // schedules
  schedules: async ({ accessToken }) => {
    try {
      const response = await fetch(`${BACKEND_URL}/schedules/`, {
        method: "GET",
        headers: { ...headers, Authorization: `Bearer ${accessToken}` },
      });

      if (!response.ok) {
        throw new Error(`${response.status}`);
      }

      const data = await response.json();

      return { res: data, err: null };
    } catch (error) {
      return { res: null, err: error };
    }
  },

  cancelSchedule: async ({ accessToken, id }) => {
    try {
      const response = await fetch(`${BACKEND_URL}/schedules/${id}/`, {
        method: "PATCH",
        headers: {
          ...headers,
          Authorization: `Bearer ${accessToken}`,
        },
        body: JSON.stringify({ Confirmed: false }),
      });

      if (!response.ok) {
        throw new Error(`${response.status}`);
      }

      const data = await response.json();

      return { res: data, err: null };
    } catch (error) {
      return { res: null, err: error };
    }
  },

  updateSchedule: async ({ accessToken, id, Date, Time, EconomyPrice }) => {
    try {
      const response = await fetch(`${BACKEND_URL}/schedules/${id}/`, {
        method: "PATCH",
        headers: {
          ...headers,
          Authorization: `Bearer ${accessToken}`,
        },
        body: JSON.stringify({ Date, Time, EconomyPrice }),
      });

      if (!response.ok) {
        throw new Error(`${response.status}`);
      }

      const data = await response.json();

      return { res: data, err: null };
    } catch (error) {
      return { res: null, err: error };
    }
  },

  importSchedules: async ({ accessToken, formData }) => {
    try {
      const response = await fetch(`${BACKEND_URL}/schedules/import/`, {
        method: "POST",
        headers: {
          ...headers,
          Authorization: `Bearer ${accessToken}`,
        },
        body: formData,
      });

      if (!response.ok) {
        throw new Error(`${response.status}`);
      }

      const data = await response.json();

      return { res: data, err: null };
    } catch (error) {
      return { res: null, err: error };
    }
  },

  // airports
  airports: async ({ accessToken }) => {
    try {
      const response = await fetch(`${BACKEND_URL}/airport/`, {
        method: "GET",
        headers: { ...headers, Authorization: `Bearer ${accessToken}` },
      });

      if (!response.ok) {
        throw new Error(`${response.status}`);
      }

      const data = await response.json();

      return { res: data, err: null };
    } catch (error) {
      return { res: null, err: error };
    }
  },
};
