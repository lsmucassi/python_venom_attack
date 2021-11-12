import json
from os import pardir

def get_data(file):
    '''
    Takes in a file name, open it
    Returns data in a dictionary form
    '''
    data = []
    try:
        with open(file, 'r') as f:
            data = json.load(f)
    except EnvironmentError:
        print(f"Error: Couldn't open file - {file}")

    return data

def filter_reservations(data):
    '''
    Takes in a disctionary and return unpaid events only
    '''
    unpaid = []
    if data:
        for event in data:
            if event['paid'] == False:
                unpaid.append(event)
    
    return unpaid


def run_app():
    # get all paid data from paid file
    paid_data = get_data('paid.json')
    # Get pending data from reservations data
    reservation_data = get_data('reservations.json')
    
    # filter reservation data 
    unpaid_data = filter_reservations(reservation_data)

    # check if user paid reservation
    '''
    we know that the data share _id
    '''
    if paid_data and unpaid_data:
        for i, event in enumerate(unpaid_data):
            payload = next((item for item in paid_data if item["_id"] == event['_id']), None)
            if payload != None:
                # if paid update status
                if event['paid'] == False and payload['paid'] == True:
                    unpaid_data[i]['paid'] = True
            # else check if date is overdue for payment
            else:


                    print("\n", unpaid_data[i])

        

        

        

        


def main():
    run_app()


if __name__ == "__main__":
    main()