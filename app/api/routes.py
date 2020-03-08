from app.api import bp
from app.api.auth import token_auth


@bp.route('/get_entry/<int:id>', methods=['GET'])
@token_auth.login_required
def get_entry(id):
    # TODO: We need to check if
    # - The specified entry exists
    # - The current user owns that entry
    pass


@bp.route('/get_entries/<int:id>', methods=['GET'])
@token_auth.login_required
def get_entries(id):
    # TODO: Get the entries for the current user. Probably a list of ints.
    # Also, check to make sure that the specified ID equals the current user's ID.
    pass
