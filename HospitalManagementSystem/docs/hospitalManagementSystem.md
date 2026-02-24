# Summary: Clinical Records, Facility Management & Booking Logic

### 1. Clinical Intelligence (Diagnosis, Allergies & Medicine)
* **Resource Repositories**: The system maintains dynamic tables for diseases, allergies, and medicines, allowing doctors to retrieve data for sick notes and medical documents.
* **Medicine Tracking**: The `availableMedecine` table tracks medications by name and the symptoms they address.
* **Standardized Procedures**: Data entry is managed through specific procedures to ensure consistency:
    * `inertA`: Creates new allergy records linked to diagnosis names and medicine IDs.
    * `inertD`: Registers new diagnosis records.
    * `insertM`: Adds new medicine to the inventory, specifying what it is effective against.

### 2. Hospital Infrastructure & Room Management
* **Floor Zoning**: Rooms are categorized by floor: 100–199 (First), 200–299 (Second), and 300–399 (Third).
* **Room Administration**: Dedicated procedures (`firstFloor`, `secondFloor`, `thirdFloor`) assign IDs and names to rooms, while `modifyFloor` handles updates to room data.
* **Unified Visibility**: A database **View** is implemented to aggregate all floors into a single, comprehensive table for staff.



### 3. Room Booking & Operation Logic
* **Operational Planning**: Staff use the `RoomBooking` table to reserve rooms for surgeries or ward stays.
* **Financial Integration**: An `operation procedures` table lists the specific prices for various medical procedures.
* **Booking Workflow**:
    * **Search**: `searchRoom()` identifies vacant rooms.
    * **Reservation**: `bookRoom()` secures a room for a patient.
    * **Cancellation**: `cancelBook()` releases a previously booked room.

### 4. Availability Functions & Safeguards
* **Validation Logic**: The function `checkAvailableRoom(roomID)` verifies room availability by cross-referencing dates in the booking table.
* **Conflict Prevention**: This function returns 1 (available) or 0 (booked) to prevent double-bookings.