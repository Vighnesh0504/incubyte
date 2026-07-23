import api from "./api";

export const getVehicles = async () => {
  const response = await api.get("vehicles/");
  return response.data;
};

export const createVehicle = async (vehicle) => {
  const response = await api.post("vehicles/", vehicle);
  return response.data;
};

export const updateVehicle = async (id, data) => {
    const response = await api.patch(`vehicles/${id}/`, data);
    return response.data;
};
export const deleteVehicle = async (id) => {
  const response = await api.delete(`vehicles/${id}/`);
  return response.data;
};

export const purchaseVehicle = async (id) => {
  const response = await api.post(`vehicles/${id}/purchase/`);
  return response.data;
};

export const restockVehicle = async (id, quantity) => {
  const response = await api.post(`vehicles/${id}/restock/`, {
    quantity,
  });

  return response.data;
};

export const searchVehicles = async (filters) => {
  const response = await api.get("vehicles/search/", {
    params: filters,
  });

  return response.data;
};

