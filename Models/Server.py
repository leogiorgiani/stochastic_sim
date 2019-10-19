from Models.Atoms import Attendant


class Server:
    attendants: list

    def __init__(self, n_attendants):
        self.attendants = [Attendant() for _ in range(n_attendants)]

    '''
        TODO:   - clients arrival
                - clients disparture
                - stats processing
                - generalized model
    '''
