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

    @classmethod
    def from_dict(cls, superfund_data):
        new_superfund = superfund_site(site_id=superfund_data["SITE_ID"],site_name=superfund_data["SITE_NAME"],
                        site_strt_adrs1=superfund_data["SITE_STRT_ADRS1"],
                        site_city_name=superfund_data["SITE_CITY_NAME"],
                        site_state=superfund_data["SITE_STATE"],
                        site_zip_code=superfund_data["SITE_ZIP_CODE"],
                        site_cong_district=superfund_data["SITE_CONG_DISTRICT"],
                        site_cnty_name=superfund_data["SITE_CNTY_NAME"],
                        latitude=superfund_data["LATITUDE"],
                        longitude=superfund_data["LONGITUDE"],
                        npl=superfund_data["NPL"]
        )
        return new_superfund
    
    def to_dict(self):
        return {
            "SITE_ID": self.site_id,
            "SITE_NAME": self.site_name,
            "SITE_STRT_ADRS1": self.site_strt_adrs1,
            "SITE_CITY_NAME": self.site_city_name,
            "SITE_STATE": self.site_state,
            "SITE_ZIP_CODE": self.site_zip_code,
            "SITE_CONG_DISTRICT": self.site_cong_district,
            "SITE_CNTY_NAME": self.site_cnty_name, 
            "LATITUDE": self.latitude,
            "LONGITUDE": self.longitude,
            "NPL": self.npl
        }