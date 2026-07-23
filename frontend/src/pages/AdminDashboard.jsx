import { useEffect, useState } from "react";
import Navbar from "../components/Navbar";
import VehicleForm from "../components/VehicleForm";

import {
  getVehicles,
  createVehicle,
  updateVehicle,
  deleteVehicle,
  restockVehicle,
  searchVehicles,
} from "../services/vehicleService";

export default function AdminDashboard() {
  const [vehicles, setVehicles] = useState([]);
  const [loading, setLoading] = useState(true);
  const [editingVehicle, setEditingVehicle] = useState(null);
  const [showForm, setShowForm] = useState(false);

  // Total count state
  const [count, setCount] = useState(0);

  // Pagination states
  const [nextPage, setNextPage] = useState(null);
  const [previousPage, setPreviousPage] = useState(null);

  // Filter state
  const [filters, setFilters] = useState({
    make: "",
    model: "",
    category: "",
  });

  useEffect(() => {
    fetchVehicles();
  }, []);

  const fetchVehicles = async (pageUrl) => {
    setLoading(true);
    try {
      const data = await getVehicles(pageUrl);

      setVehicles(data.results || data);
      setCount(data.count ?? (Array.isArray(data) ? data.length : 0));
      setNextPage(data.next || null);
      setPreviousPage(data.previous || null);
    } catch (error) {
      console.error("Failed to fetch vehicles:", error);
      alert(error.response?.data?.detail || "Something went wrong while fetching vehicles.");
    } finally {
      setLoading(false);
    }
  };

  const handleSearch = async () => {
    setLoading(true);
    try {
      const data = await searchVehicles(filters);
      setVehicles(data.results ?? data);
      setCount(data.count ?? (Array.isArray(data) ? data.length : 0));
      setNextPage(data.next || null);
      setPreviousPage(data.previous || null);
    } catch (err) {
      console.error("Search error:", err);
      alert(err.response?.data?.detail || "Something went wrong during search.");
    } finally {
      setLoading(false);
    }
  };

  const handleResetSearch = () => {
    setFilters({
      make: "",
      model: "",
      category: "",
    });
    fetchVehicles();
  };

  const handleDelete = async (id) => {
    const confirmDelete = window.confirm(
      "Are you sure you want to delete this vehicle?"
    );

    if (!confirmDelete) return;

    try {
      await deleteVehicle(id);
      fetchVehicles();
    } catch (err) {
      console.error("Delete error:", err);
      alert(err.response?.data?.detail || "Failed to delete vehicle.");
    }
  };

  const handleRestock = async (vehicle) => {
    const quantity = prompt("Enter quantity to add:");

    if (!quantity || isNaN(quantity) || Number(quantity) <= 0) return;

    try {
      await restockVehicle(vehicle.id, Number(quantity));
      fetchVehicles();
    } catch (err) {
      console.error("Restock error:", err);
      alert(err.response?.data?.detail || "Failed to restock vehicle.");
    }
  };

  const handleCreate = async (data) => {
    try {
      await createVehicle(data);
      alert("Vehicle created successfully!");
      setShowForm(false);
      fetchVehicles();
    } catch (error) {
      console.error("Create error:", error.response?.data || error);
      alert(error.response?.data?.detail || "Failed to create vehicle.");
    }
  };

  const handleUpdate = async (data) => {
    try {
      await updateVehicle(editingVehicle.id, data);
      alert("Vehicle updated successfully!");
      setEditingVehicle(null);
      setShowForm(false);
      fetchVehicles();
    } catch (error) {
      console.error("Update error:", error.response?.data || error);
      alert(error.response?.data?.detail || "Failed to update vehicle.");
    }
  };

  const handleCancel = () => {
    setEditingVehicle(null);
    setShowForm(false);
  };

  // Step 1: Calculate Statistics based on currently loaded list
  const totalVehicles = vehicles.length;
  const totalStock = vehicles.reduce(
    (sum, vehicle) => sum + vehicle.quantity,
    0
  );
  const outOfStock = vehicles.filter(
    (vehicle) => vehicle.quantity === 0
  ).length;

  // Full Page Loading State
  if (loading && vehicles.length === 0) {
    return (
      <div className="flex justify-center items-center h-screen bg-gray-50 text-lg font-medium text-gray-600">
        Loading...
      </div>
    );
  }

  return (
    <>
      <Navbar />

      <div className="max-w-7xl mx-auto p-8">
        <div className="flex justify-between items-center mb-6">
          <h1 className="text-4xl font-bold">Admin Dashboard</h1>
          {!showForm && (
            <button
              onClick={() => {
                setEditingVehicle(null);
                setShowForm(true);
              }}
              className="bg-blue-600 text-white px-5 py-2.5 rounded-lg font-medium hover:bg-blue-700 transition-colors"
            >
              + Add Vehicle
            </button>
          )}
        </div>

        {/* Step 2: Statistics Cards */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-6">
          <div className="bg-white shadow rounded-xl p-6 border border-gray-100">
            <h3 className="text-gray-500 font-medium">Total Vehicles</h3>
            <p className="text-3xl font-bold mt-1">{totalVehicles}</p>
          </div>

          <div className="bg-white shadow rounded-xl p-6 border border-gray-100">
            <h3 className="text-gray-500 font-medium">Available Stock</h3>
            <p className="text-3xl font-bold mt-1">{totalStock}</p>
          </div>

          <div className="bg-white shadow rounded-xl p-6 border border-gray-100">
            <h3 className="text-gray-500 font-medium">Out of Stock</h3>
            <p className="text-3xl font-bold mt-1 text-red-600">{outOfStock}</p>
          </div>
        </div>

        {/* Filter / Search Bar */}
        <div className="flex flex-wrap gap-4 mb-6 bg-white p-4 rounded-xl shadow-sm border border-gray-100">
          <input
            type="text"
            placeholder="Search Make"
            value={filters.make}
            onChange={(e) =>
              setFilters({ ...filters, make: e.target.value })
            }
            className="border rounded-lg p-2.5 flex-1 min-w-[150px] focus:outline-none focus:ring-2 focus:ring-blue-500"
          />

          <input
            type="text"
            placeholder="Search Model"
            value={filters.model}
            onChange={(e) =>
              setFilters({ ...filters, model: e.target.value })
            }
            className="border rounded-lg p-2.5 flex-1 min-w-[150px] focus:outline-none focus:ring-2 focus:ring-blue-500"
          />

          <select
            value={filters.category}
            onChange={(e) =>
              setFilters({ ...filters, category: e.target.value })
            }
            className="border rounded-lg p-2.5 flex-1 min-w-[150px] focus:outline-none focus:ring-2 focus:ring-blue-500"
          >
            <option value="">All Categories</option>
            <option value="Sedan">Sedan</option>
            <option value="SUV">SUV</option>
            <option value="Hatchback">Hatchback</option>
          </select>

          <button
            onClick={handleSearch}
            className="bg-blue-600 hover:bg-blue-700 text-white px-5 py-2.5 rounded-lg font-medium transition-colors"
          >
            Search
          </button>

          <button
            onClick={handleResetSearch}
            className="bg-gray-200 hover:bg-gray-300 text-gray-700 px-4 py-2.5 rounded-lg font-medium transition-colors"
          >
            Reset
          </button>
        </div>

        {/* Add / Edit Form Drawer */}
        {showForm && (
          <div className="bg-white p-6 rounded-xl shadow-md border border-gray-100 mb-8 max-w-2xl">
            <div className="flex justify-between items-center mb-4">
              <h2 className="text-2xl font-semibold">
                {editingVehicle ? "Edit Vehicle" : "Add New Vehicle"}
              </h2>
              <button
                onClick={handleCancel}
                className="text-gray-500 hover:text-gray-700 text-sm font-medium"
              >
                Cancel
              </button>
            </div>

            <VehicleForm
              vehicle={editingVehicle}
              onSubmit={editingVehicle ? handleUpdate : handleCreate}
              buttonText={editingVehicle ? "Update Vehicle" : "Create Vehicle"}
            />
          </div>
        )}

        {/* Total Count Display */}
        <p className="text-gray-600 mb-4 font-medium">
          Total Vehicles Count (API): {count}
        </p>

        {/* Vehicle Management List & Empty State */}
        {vehicles.length === 0 ? (
          <p className="text-center text-gray-500 py-10 text-lg">
            No vehicles available.
          </p>
        ) : (
          <>
            <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
              {vehicles.map((vehicle) => (
                <div
                  key={vehicle.id}
                  className="bg-white rounded-xl shadow-md p-5 border border-gray-100 flex flex-col justify-between"
                >
                  <div>
                    <h3 className="text-xl font-bold">
                      {vehicle.make} {vehicle.model}
                    </h3>
                    <p className="text-gray-600 mt-1">
                      Category: {vehicle.category}
                    </p>
                    <p className="mt-1 font-semibold">Price: ₹{vehicle.price}</p>
                    <p className="mt-1">
                      Stock:{" "}
                      <span
                        className={
                          vehicle.quantity > 0
                            ? "text-green-600 font-semibold"
                            : "text-red-600 font-semibold"
                        }
                      >
                        {vehicle.quantity}
                      </span>
                    </p>
                  </div>

                  <div className="mt-4 pt-4 border-t border-gray-100 flex justify-end space-x-2">
                    <button
                      onClick={() => handleRestock(vehicle)}
                      className="rounded bg-green-600 px-3 py-1 text-white hover:bg-green-700 transition-colors font-medium text-sm"
                    >
                      Restock
                    </button>

                    <button
                      onClick={() => {
                        setEditingVehicle(vehicle);
                        setShowForm(true);
                      }}
                      className="rounded bg-yellow-500 px-3 py-1 text-white hover:bg-yellow-600 transition-colors font-medium text-sm"
                    >
                      Edit
                    </button>

                    <button
                      onClick={() => handleDelete(vehicle.id)}
                      className="rounded bg-red-600 px-3 py-1 text-white hover:bg-red-700 transition-colors font-medium text-sm"
                    >
                      Delete
                    </button>
                  </div>
                </div>
              ))}
            </div>

            {/* Pagination Controls */}
            <div className="flex justify-between items-center mt-8">
              <button
                disabled={!previousPage}
                onClick={() => fetchVehicles(previousPage)}
                className="bg-gray-500 hover:bg-gray-600 text-white px-4 py-2 rounded-lg transition-colors disabled:opacity-50 disabled:cursor-not-allowed"
              >
                Previous
              </button>

              <button
                disabled={!nextPage}
                onClick={() => fetchVehicles(nextPage)}
                className="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-lg transition-colors disabled:opacity-50 disabled:cursor-not-allowed"
              >
                Next
              </button>
            </div>
          </>
        )}
      </div>
    </>
  );
}