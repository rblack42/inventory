from flask import (
    Blueprint, 
    flash, 
    g, 
    redirect, 
    render_template, 
    request, 
    url_for
)

from werkzeug.exceptions import abort

from inventory.auth import login_required
from inventory.db import get_db

bp = Blueprint('inventory', __name__)

@bp.route('/')
def index():
    db = get_db()
    items = db.execute(
        'SELECT i.id, name, uuid, created, author_id, username'
        ' FROM item i JOIN user u ON i.author_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()
    return render_template('items/index.html', items=items)

@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        name = request.form['name']
        uuid = request.form['uuid']
        error = None

        if not name:
            error = 'uuid is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO item (name, uuid, author_id)'
                ' VALUES (?, ?, ?)',
                (name, uuid, g.user['id'])
            )
            db.commit()
            return redirect(url_for('inventory.index'))

    return render_template('items/create.html')

def get_item(id, check_author=True):
    item = get_db().execute(
        'SELECT i.id, name, uuid, created, author_id, username'
        ' FROM item i JOIN user u ON i.author_id = u.id'
        ' WHERE i.id = ?',
        (id,)
    ).fetchone()

    if item is None:
        abort(404, f"Item id {id} doesn't exist.")

    if check_author and item['author_id'] != g.user['id']:
        abort(403)

    return item

@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    item = get_item(id)

    if request.method == 'POST':
        name = request.form['name']
        uuid = request.form['uuid']
        error = None

        if not name:
            error = 'Name is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'UPDATE item SET name = ?, uuid = ?'
                ' WHERE id = ?',
                (name, uuid, id)
            )
            db.commit()
            return redirect(url_for('inventory.index'))

    return render_template('items/update.html', item=item)
