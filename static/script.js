const form = document.getElementById("predictionForm");

form.addEventListener("submit", async function (event) {

    event.preventDefault();

    const data = {

        hotel: document.getElementById("hotel").value,

        lead_time: Number(document.getElementById("lead_time").value),

        arrival_date_year: Number(document.getElementById("arrival_date_year").value),

        arrival_date_month: document.getElementById("arrival_date_month").value,

        arrival_date_week_number: Number(document.getElementById("arrival_date_week_number").value),

        arrival_date_day_of_month: Number(document.getElementById("arrival_date_day_of_month").value),

        stays_in_weekend_nights: Number(document.getElementById("stays_in_weekend_nights").value),

        stays_in_week_nights: Number(document.getElementById("stays_in_week_nights").value),

        adults: Number(document.getElementById("adults").value),

        children: Number(document.getElementById("children").value),

        babies: Number(document.getElementById("babies").value),

        meal: document.getElementById("meal").value,

        country: document.getElementById("country").value,

        market_segment: document.getElementById("market_segment").value,

        distribution_channel: document.getElementById("distribution_channel").value,

        is_repeated_guest: Number(document.getElementById("is_repeated_guest").value),

        previous_cancellations: Number(document.getElementById("previous_cancellations").value),

        previous_bookings_not_canceled: Number(document.getElementById("previous_bookings_not_canceled").value),

        reserved_room_type: document.getElementById("reserved_room_type").value,

        assigned_room_type: document.getElementById("assigned_room_type").value,

        booking_changes: Number(document.getElementById("booking_changes").value),

        deposit_type: document.getElementById("deposit_type").value,

        days_in_waiting_list: Number(document.getElementById("days_in_waiting_list").value),

        customer_type: document.getElementById("customer_type").value,

        adr: Number(document.getElementById("adr").value),

        required_car_parking_spaces: Number(document.getElementById("required_car_parking_spaces").value),

        total_of_special_requests: Number(document.getElementById("total_of_special_requests").value)

    };

    try {

        const response = await fetch("/predict", {

            method: "POST",

            headers: {

                "Content-Type": "application/json"

            },

            body: JSON.stringify(data)

        });

        const result = await response.json();

        document.getElementById("result-card").style.display = "block";

        if (result.prediction === 1) {

            document.getElementById("predictionText").innerHTML =
                "❌ Booking will probably be Cancelled";

        }
        else {

            document.getElementById("predictionText").innerHTML =
                "✅ Booking will probably NOT be Cancelled";

        }

        document.getElementById("cancelProb").innerHTML =
            (result.cancel_probability * 100).toFixed(1) + "%";

        document.getElementById("notCancelProb").innerHTML =
            (result.not_cancel_probability * 100).toFixed(1) + "%";

    }

    catch (error) {

        alert("Server Error");

        console.error(error);

    }

});