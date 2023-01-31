from app import db

class superfund_site(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True) 
    site_id = db.Column(db.String)
    site_name = db.Column(db.String)
    site_strt_adrs1 = db.Column(db.String)
    site_city_name = db.Column(db.String)
    site_state= db.Column(db.String)
    site_zip_code = db.Column(db.String)
    site_cong_district = db.Column(db.String)
    site_cnty_name = db.Column(db.String)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    npl = db.Column(db.String)

