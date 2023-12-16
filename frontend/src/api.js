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
        throw new Error(`${data.error} (${response.status}) `);
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

  me: async ({ accessToken }) => {
    try {
      const response = await fetch(`${BACKEND_URL}/auth/me/`, {
        method: "GET",
        headers: { ...headers, Authorization: `Bearer ${accessToken}` },
      });

      if (!response.ok) {
        throw new Error(`(${response.status}) User is not logged in`);
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

  sendLogoutInformation: async ({ accessToken, id, reason, loginTime }) => {
    try {
      const response = await fetch(
        `${BACKEND_URL}/users/change-logout-info/${id}/`,
        {
          method: "PUT",
          headers: {
            ...headers,
            Authorization: `Bearer ${accessToken}`,
          },
          body: JSON.stringify({ reason, loginTime }),
        }
      );

      if (!response.ok) {
        throw new Error(`(${response.status}) Error sending logout info`);
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
  getAllSchedules: async ({ accessToken }) => {
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

  cancelFlight: async ({ accessToken, id }) => {
    try {
      const response = await fetch(`${BACKEND_URL}/schedules/cancel/${id}/`, {
        method: "POST",
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

  updateFlight: async ({ accessToken, id, ...payload }) => {
    try {
      const response = await fetch(`${BACKEND_URL}/schedules/${id}/`, {
        method: "PATCH",
        headers: {
          ...headers,
          Authorization: `Bearer ${accessToken}`,
        },
        body: JSON.stringify(payload[0]),
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
      const response = await fetch(`${BACKEND_URL}/schedules/import-csv/`, {
        method: "POST",
        headers: {
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
  getAllAirports: async () => {
    try {
      const response = await fetch(`${BACKEND_URL}/airports/`, {
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

  // countries
  getAllCountries: async () => {
    try {
      const response = await fetch(`${BACKEND_URL}/countries/`, {
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

  // tickets
  searchForTickets: async ({ accessToken, payload }) => {
    try {
      const response = await fetch(`${BACKEND_URL}/tickets/search/`, {
        method: "POST",
        headers: {
          ...headers,
          Authorization: `Bearer ${accessToken}`,
        },
        body: JSON.stringify({
          from_airport: payload.from,
          to_airport: payload.to,
          cabin_type: payload.cabinType,
          outbound_date: payload.onboardDate,
          return_date: payload.returnDate,
          wide_search: true,
        }),
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

  issueTicket: async ({ accessToken, payload }) => {
    console.log(payload);
    try {
      const response = await fetch(`${BACKEND_URL}/tickets/issue-ticket/`, {
        method: "POST",
        headers: {
          ...headers,
          Authorization: `Bearer ${accessToken}`,
        },
        body: JSON.stringify({
          user: payload.user,
          schedule: payload.schedule,
          cabin_type: payload.cabinType,
          first_name: payload.firstName,
          last_name: payload.lastName,
          phone: payload.phoneNumber,
          passport_number: payload.passportNumber,
          passport_country_id: payload.passportCountry,
          booking_reference: payload.bookingReference,
          confirmed: true,
        }),
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

  // amenities
  getShortSummary: async (accessToken) => {
    try {
      const response = await fetch(`${BACKEND_URL}/amenities/short-summary/`, {
        method: "GET",
        headers: {
          ...headers,
          Authorization: `Bearer ${accessToken}`,
        },
      });

      if (!response.ok) {
        throw new Error(`${response.status}`);
      }

      const data = await response.json();
      console.log(data);

      return { res: data, err: null };
    } catch (error) {
      return { res: null, err: error };
    }
  },

  getAmenitiesReport: async ({ accessToken, payload }) => {
    try {
      const response = await fetch(
        `${BACKEND_URL}/amenities/amenities-report/`,
        {
          method: "POST",
          headers: {
            ...headers,
            Authorization: `Bearer ${accessToken}`,
          },
          body: JSON.stringify({
            flight_id: payload.flightID,
            start_date: payload.startDate,
            end_date: payload.endDate,
          }),
        }
      );

      if (!response.ok) {
        throw new Error(`${response.status}`);
      }

      const data = await response.json();
      console.log(data);

      return { res: data, err: null };
    } catch (error) {
      console.log(error);

      return { res: null, err: error };
    }
  },

  searchForAmenity: async ({ accessToken, payload }) => {
    try {
      const response = await fetch(`${BACKEND_URL}/amenities/search/`, {
        method: "POST",
        headers: {
          ...headers,
          Authorization: `Bearer ${accessToken}`,
        },
        body: JSON.stringify({
          from_airport: payload.from,
          to_airport: payload.to,
          cabin_type: payload.cabinType,
          outbound_date: payload.onboardDate,
          return_date: payload.returnDate,
          wide_search: true,
        }),
      });

      if (!response.ok) {
        throw new Error(`${response.status}`);
      }

      const data = await response.json();
      console.log(data);

      return { res: data, err: null };
    } catch (error) {
      return { res: null, err: error };
    }
  },

  purchaseAmenity: async ({ accessToken, id, payload }) => {
    try {
      const response = await fetch(
        `${BACKEND_URL}/amenities/purchase-amenities-for-ticket/${id}`,
        {
          method: "POST",
          headers: {
            ...headers,
            Authorization: `Bearer ${accessToken}`,
          },
          body: JSON.stringify({
            amenities_id: payload.amenitiesID,
          }),
        }
      );

      if (!response.ok) {
        throw new Error(`${response.status}`);
      }

      const data = await response.json();
      console.log(data);

      return { res: data, err: null };
    } catch (error) {
      return { res: null, err: error };
    }
  },
};
