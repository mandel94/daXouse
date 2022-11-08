class IdDigestError(Exception):
    '''Raised for exceptions during digest of unique house identifier'''

    def __init__(self, prop, *args: object) -> None:
        super().__init__(*args)
        self.prop = prop

    def __str__(self) -> str:
        return  (f'Some error occurred when producing the digest '\
                 'of house identifier w/ value={self.prop}')