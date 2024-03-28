from flask import Flask, jsonify, request
from flask_cors import CORS
import mysql.connector
from datetime import date

app = Flask(__name__)
CORS(app)

#connect to mysql
connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Ahuva123!",
    database="corona_db"
)

#method for create template for insert member
def update_and_add_member(member_data):
    #ebstract the data from member_data
    id = member_data.get('id')
    first_name = member_data.get('first_name')
    last_name = member_data.get('last_name')
    address = member_data.get('address')
    date_of_birth = member_data.get('date_of_birth')
    telephone = member_data.get('telephone')
    mobile_phone = member_data.get('mobile_phone')
    if member_data.get('vaccine_1_date') != "":
        vaccine_1_date = member_data.get('vaccine_1_date')
    else:
        vaccine_1_date = None
    if member_data.get('vaccine_1_manufacturer') != "no-choice":
        vaccine_1_manufacturer = member_data.get('vaccine_1_manufacturer')
    else:
        vaccine_1_manufacturer = None
    if member_data.get('vaccine_2_date') != "":
        vaccine_2_date = member_data.get('vaccine_2_date')
    else:
        vaccine_2_date = None
    if member_data.get('vaccine_2_manufacturer') != "no-choice":
        vaccine_2_manufacturer = member_data.get('vaccine_2_manufacturer')
    else:
        vaccine_2_manufacturer = None
    if member_data.get('vaccine_3_date') != "":
        vaccine_3_date = member_data.get('vaccine_3_date')
    else:
        vaccine_3_date = None
    if member_data.get('vaccine_3_manufacturer') != "no-choice":
        vaccine_3_manufacturer = member_data.get('vaccine_3_manufacturer')
    else:
        vaccine_3_manufacturer = None
    if member_data.get('vaccine_4_date') != "":
        vaccine_4_date = member_data.get('vaccine_4_date')
    else:
        vaccine_4_date = None
    if member_data.get('vaccine_4_manufacturer') != "no-choice":
        vaccine_4_manufacturer = member_data.get('vaccine_4_manufacturer')
    else:
        vaccine_4_manufacturer = None
    if member_data.get('positive_result_date') != "":
        positive_result_date = member_data.get('positive_result_date')
    else:
        positive_result_date = None
    if member_data.get('recovery_date') != "":
        recovery_date  =member_data.get('recovery_date')
    else:
        recovery_date = None

    #create new member
    new_member = (id,
         first_name,
         last_name,
         address,
         date_of_birth,
         telephone,
         mobile_phone,
         vaccine_1_date,
         vaccine_1_manufacturer,
         vaccine_2_date,
         vaccine_2_manufacturer,
         vaccine_3_date,
         vaccine_3_manufacturer,
         vaccine_4_date,
         vaccine_4_manufacturer,
         positive_result_date,
         recovery_date)
    return new_member

#create insert query for insert new member
def create_insert_query():
    insert_query = """
            INSERT INTO members (id,
             first_name,
             last_name,
             address,
             date_of_birth,
             telephone,
             mobile_phone,
             vaccine_1_date,
             vaccine_1_manufacturer,
             vaccine_2_date,
             vaccine_2_manufacturer,
             vaccine_3_date,
             vaccine_3_manufacturer,
             vaccine_4_date,
             vaccine_4_manufacturer,
             positive_result_date,
             recovery_date)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
    return insert_query

#create delete query for delete member
def create_delete_query():
    delete_query = "DELETE FROM members WHERE id = %s"
    return  delete_query

#GET request - get all members
@app.route('/client', methods=['GET'])
def get_members():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM members")
    columns = [column[0] for column in cursor.description]
    members = cursor.fetchall()

    # Convert the result into a list of dictionaries
    members_list = []
    for member in members:
        member_dict = dict(zip(columns, member))
        members_list.append(member_dict)
    cursor.close()
    return jsonify(members_list)


#POST request - add member to database
@app.route('/client', methods=['POST'])
def add_member():
    cursor = connection.cursor()
    # Get data from the request body
    member_data = request.json
    print(member_data)
    new_member= update_and_add_member(member_data)

    #insert the new member to members table
    try:
        cursor.execute(create_insert_query(), new_member)
        connection.commit()
        return jsonify({'message': 'Member added successfully'}), 201

    #if the insertion did not succeed
    except Exception as e:
        connection.rollback()
        return jsonify({'error': str(e)}), 400
    finally:
        cursor.close()

#PUT request - update a member
@app.route('/client', methods=['PUT'])
def update_member():
        cursor = connection.cursor()
        # Get data from the request body
        member_data = request.json
        id_member = member_data.get('id')

        try:
            # delete current member
            cursor.execute(create_delete_query(), (id_member,))
            connection.commit()
            # insert update member
            update_member = update_and_add_member(member_data)
            cursor.execute(create_insert_query(), update_member)
            connection.commit()
            return jsonify({'message': 'Member updated successfully'}), 200

        except Exception as e:
            connection.rollback()
            return jsonify({'error': str(e)}), 500
        finally:
            cursor.close()

#DELETE request - delete a member
@app.route('/client/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    try:
        cursor = connection.cursor()
        cursor.execute(create_delete_query(), (member_id,))
        connection.commit()
        return jsonify({'message': 'Member deleted successfully'}), 200
    except Exception as e:
        connection.rollback()
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()


if __name__ == '__main__':
    app.run(debug=True)
