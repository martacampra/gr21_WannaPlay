from flask import Blueprint, render_template
from flaskblog.models import Event,Participant,SportPlayed, Sport
from flask_login import login_required,current_user
main = Blueprint('main', __name__)

places = [
    {
        'name': 'Centro Sportivo Robilant',
        'address': 'Piazza Robilant 16, Torino (TO), 10141',
        'telephone': '011 385 0763'

    },
    {
        'name': 'Monviso Sporting Club',
        'address': 'Corso Giuseppe Allamano, 25, Grugliasco (TO), 10095',
        'telephone': '011 788 034'
    },
    {
        'name': 'Royal Club',
        'address': 'Piazza Muzio Scevola,2, Torino (TO), 10133',
        'telephone': '011 661 8432'
    },
    {
        'name': 'Master Club 2.0',
        'address': 'Corso Moncalieri 494, Torino (TO), 10133',
        'telephone': '011 661 0963'
    },

    {
        'name': 'Esperia Torino',
        'address': 'Corso Moncalieri,2, Torino(TO), 10131',
        'telephone': '011 819 3013'
    }
]

@main.route("/home")
@login_required
def home():
    posts = Event.query.all()
    participant_list = {}
    for p in posts:
        participant_list[p.id] = [Participant.query.filter_by(e_id=p.id).all()]
        participant_list[p.id].append(len(participant_list[p.id][0]))
    return render_template('home.html', posts=posts, join=participant_list)

@main.route("/match")
@login_required
def match():
    sport = SportPlayed.query.filter_by(u_id=current_user.id).all()
    posts=[]
    for s in sport:
        posts.append(Event.query.filter_by(sport_id=s.s_id).all())

        participant_list = {}
        for p in posts:
            for c in p:
                participant_list[c.id] = [Participant.query.filter_by(e_id=c.id).all()]
                participant_list[c.id].append(len(participant_list[c.id][0]))
    return render_template('match.html', posts=posts, join=participant_list)




@main.route("/contact")
def contact():
    return render_template('contact.html', title='Contact sports club', places=places)


@main.route("/about")
def about():
    return render_template('about.html', title='About Us')


@main.route("/", methods=['GET', 'POST'])
def start():
    return render_template('start.html', title='Start')