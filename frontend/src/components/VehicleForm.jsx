import { useState, useEffect } from "react";

export default function VehicleForm({
  vehicle,
  onSubmit,
  buttonText = "Save",
}) {
  const [form, setForm] = useState({
    make: "",
    model: "",
    category: "",
    price: "",
    quantity: "",
  });

  // Sync form values when the `vehicle` prop updates (e.g., when clicking Edit)
  useEffect(() => {
    if (vehicle) {
      setForm(vehicle);
    } else {
      // Reset form if switching back to "Create" mode
      setForm({
        make: "",
        model: "",
        category: "",
        price: "",
        quantity: "",
      });
    }
  }, [vehicle]);

  const handleChange = (e) => {
    setForm({
      ...form,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    onSubmit({
      ...form,
      price: Number(form.price),
      quantity: Number(form.quantity),
    });
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-4">
      <div>
        <label className="block text-sm font-medium text-gray-700 mb-1">
          Make
        </label>
        <input
          name="make"
          placeholder="e.g. Toyota"
          value={form.make}
          onChange={handleChange}
          className="w-full border border-gray-300 rounded-lg p-3 focus:outline-none focus:ring-2 focus:ring-blue-500"
          required
        />
      </div>

      <div>
        <label className="block text-sm font-medium text-gray-700 mb-1">
          Model
        </label>
        <input
          name="model"
          placeholder="e.g. Camry"
          value={form.model}
          onChange={handleChange}
          className="w-full border border-gray-300 rounded-lg p-3 focus:outline-none focus:ring-2 focus:ring-blue-500"
          required
        />
      </div>

      <div>
        <label className="block text-sm font-medium text-gray-700 mb-1">
          Category
        </label>
        <input
          name="category"
          placeholder="e.g. Sedan"
          value={form.category}
          onChange={handleChange}
          className="w-full border border-gray-300 rounded-lg p-3 focus:outline-none focus:ring-2 focus:ring-blue-500"
          required
        />
      </div>

      <div>
        <label className="block text-sm font-medium text-gray-700 mb-1">
          Price (₹)
        </label>
        <input
          type="number"
          name="price"
          placeholder="e.g. 1500000"
          value={form.price}
          onChange={handleChange}
          className="w-full border border-gray-300 rounded-lg p-3 focus:outline-none focus:ring-2 focus:ring-blue-500"
          required
        />
      </div>

      <div>
        <label className="block text-sm font-medium text-gray-700 mb-1">
          Quantity / Stock
        </label>
        <input
          type="number"
          name="quantity"
          placeholder="e.g. 5"
          value={form.quantity}
          onChange={handleChange}
          className="w-full border border-gray-300 rounded-lg p-3 focus:outline-none focus:ring-2 focus:ring-blue-500"
          required
        />
      </div>

      <button
        type="submit"
        className="w-full bg-blue-600 text-white py-3 rounded-lg hover:bg-blue-700 transition-colors font-medium mt-2"
      >
        {buttonText}
      </button>
    </form>
  );
}