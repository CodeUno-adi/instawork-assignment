import requests
import json

API_URL_BASE = "http://localhost:8000/api"

UNIQUE_MEMBER_ID = ''

def pretty_print_response(r):
    print("--------------------------\n")
    print("STATUS CODE IS ", r.status_code, "\n")
    try:
        print("RESPONSE IS ", json.dumps(r.json(), indent=4))
    except Exception as e:
        print("RESPONSE IS EMPTY")



# Create team member API test
def test_create_team_member():
    print("\nTESTING CREATE MEMBER API")
    team_member_data = {
        "first_name": "Aditya",
        "last_name": "N",
        "email": "gojeta.aditya@gmail.com",
        "phone_no": "+919042726176",
        "role": "regular"
    }

    r = requests.post(
        API_URL_BASE + "/team-members/",
        json = team_member_data
    )

    pretty_print_response(r)

# Get all team members API test
def test_get_all_team_members():
    print("\nTESTING GET ALL MEMBERS API")
    global UNIQUE_MEMBER_ID
    r = requests.get(API_URL_BASE + "/team-members/")
    pretty_print_response(r)
    UNIQUE_MEMBER_ID = str(r.json()[1]['id'])


# Update team member API test
def test_update_team_member():
    print("\nTESTING UPDATE MEMBER API")
    team_member_data = {
        "email": "naditya.vinc1995@gmail.co",
        "phone_no": "+917397599973",
        "role": "admin"
    }

    r = requests.patch(
        API_URL_BASE + "/team-member/" + UNIQUE_MEMBER_ID + "/",
        json = team_member_data
    )

    pretty_print_response(r)

# Delete team member API test
def test_delete_team_memeber():
    print("\nTESTING DELETE MEMBER API")
    r = requests.delete(
        API_URL_BASE + "/team-member/" + UNIQUE_MEMBER_ID + "/"
    )

    pretty_print_response(r)


if __name__ == "__main__":
    test_create_team_member()
    test_get_all_team_members()
    test_update_team_member()
    test_delete_team_memeber()




