import { useEffect, useState } from "react";
import { getVehicles, searchVehicles } from "../services/vehicleService";
import Navbar from "../components/Navbar";
import VehicleCard from "../components/VehicleCard";

export default function Dashboard() {
  const [vehicles, setVehicles] = useState([]);
  const [loading, setLoading] = useState(true);

  // Pagination states
  const [nextPage, setNextPage] = useState(null);
  const [previousPage, setPreviousPage] = useState(null);
  const [count, setCount] = useState(0);

  // Search filter state
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
    } catch (err) {
      console.error("Error fetching vehicles:", err);
      alert(err.response?.data?.detail || "Something went wrong while fetching vehicles.");
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

  // Step 1: Calculate Statistics based on current loaded items
  const totalVehicles = vehicles.length;
  const totalStock = vehicles.reduce(
    (sum, vehicle) => sum + vehicle.quantity,
    0
  );
  const outOfStock = vehicles.filter(
    (vehicle) => vehicle.quantity === 0
  ).length;

  if (loading && vehicles.length === 0) {
    return (
      <div className="flex justify-center items-center h-screen bg-gray-100 text-lg font-medium text-gray-600">
        Loading...
      </div>
    );
  }

  return (
    <>
      <Navbar />

      <div className="min-h-screen bg-gray-100 p-6">
        <h1 className="text-3xl font-bold mb-6">Vehicle Inventory</h1>

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

        {/* Search Inputs Bar */}
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

        {/* Total Count Display */}
        <p className="text-gray-600 mb-4 font-medium">
          Total Vehicles Count (API): {count}
        </p>

        {/* Vehicle Grid & Empty State */}
        {vehicles.length === 0 ? (
          <p className="text-center text-gray-500 py-10 text-lg">
            No vehicles available.
          </p>
        ) : (
          <>
            <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
              {vehicles.map((vehicle) => (
                <VehicleCard
                  key={vehicle.id}
                  vehicle={vehicle}
                  refreshVehicles={fetchVehicles}
                />
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