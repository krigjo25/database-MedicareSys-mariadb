# Hospital Management System Documentation

## 1. Clinical Intelligence
### Diagnosis, Allergies & Medicine
- **Resource Repositories**: Dynamic tables for diseases, allergies, and medicines allow doctors to retrieve data for sick notes and medical documents.
- **Medicine Tracking**: The `availableMedecine` table tracks medications by name and the symptoms they address.
- **Standardized Procedures**:
  - `inertA`: Add allergy records linked to diagnosis names and medicine IDs.
  - `inertD`: Register new diagnosis records.
  - `insertM`: Add new medicine to the inventory, specifying what it is effective against.

## 2. Hospital Infrastructure & Room Management
### Floor Zoning
- Rooms are categorized by floor:
  - 100–199: First Floor
  - 200–299: Second Floor
  - 300–399: Third Floor
### Room Administration
- Procedures:
  - `firstFloor`, `secondFloor`, `thirdFloor`: Assign IDs and names to rooms
  - `modifyFloor`: Update room data
### Unified Visibility
- A database **View** aggregates all floors into a single, comprehensive table for staff.

## 3. Room Booking & Operation Logic
### Operational Planning
- Staff use the `RoomBooking` table to reserve rooms for surgeries or ward stays.
### Financial Integration
- The `operation procedures` table lists specific prices for various medical procedures.
### Booking Workflow
  - **Search**: `searchRoom()` identifies vacant rooms.
  - **Reservation**: `bookRoom()` secures a room for a patient.
  - **Cancellation**: `cancelBook()` releases a previously booked room.

## 4. Availability Functions & Safeguards
### Validation Logic
- The function `checkAvailableRoom(roomID)` verifies room availability by cross-referencing dates in the booking table.
### Conflict Prevention
- This function returns 1 (available) or 0 (booked) to prevent double-bookings.
