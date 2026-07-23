import { purchaseVehicle } from "../services/vehicleService";

export default function VehicleCard({ vehicle, refreshVehicles }) {
  const handlePurchase = async () => {
    try {
      await purchaseVehicle(vehicle.id);
      await refreshVehicles();
    } catch (err) {
      alert(err.response?.data?.detail || "Purchase failed");
    }
  };

  return (
    <div className="bg-white rounded-xl shadow-lg p-5 hover:shadow-xl transition">
      <h2 className="text-xl font-bold">
        {vehicle.make} {vehicle.model}
      </h2>

      <p className="text-gray-500 mt-2">
        {vehicle.category}
      </p>

      <p className="mt-3 font-semibold">
        ₹{vehicle.price}
      </p>

      <p className="mt-2">
        Stock:
        <span
          className={
            vehicle.quantity > 0
              ? "text-green-600 ml-2"
              : "text-red-600 ml-2"
          }
        >
          {vehicle.quantity}
        </span>
      </p>

      <button
        onClick={handlePurchase}
        disabled={vehicle.quantity === 0}
        className={`mt-5 w-full rounded-lg py-2 text-white ${
          vehicle.quantity
            ? "bg-blue-600 hover:bg-blue-700"
            : "bg-gray-400 cursor-not-allowed"
        }`}
      >
        Purchase
      </button>
    </div>
  );
}