from sqlalchemy import Column, Integer, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class kdd_dataset(Base):
    __tablename__ = "kdd_dataset"

    id = Column('id', Integer, primary_key=True)
    duration = Column('duration', Float)
    protocol_type = Column('protocol_type', Integer)
    service = Column('service', Integer)
    flag = Column('flag', Integer)
    src_bytes = Column('src_bytes', Float)
    dst_bytes = Column('dst_bytes', Float)
    land = Column('land', Float)
    wrong_fragment = Column('wrong_fragment', Float)
    urgent = Column('urgent', Float)
    hot = Column('hot', Float)
    num_failed_logins = Column('num_failed_logins', Float)
    logged_in = Column('logged_in', Float)
    num_compromised = Column('num_compromised', Float)
    root_shell = Column('root_shell', Float)
    su_attempted = Column('su_attempted', Float)
    num_root = Column('num_root', Float)
    num_file_creations = Column('num_file_creations', Float)
    num_shells = Column('num_shells', Float)
    num_access_files = Column('num_access_files', Float)
    num_outbound_cmds = Column('num_outbound_cmds', Float)
    is_host_login = Column('is_host_login', Float)
    is_guest_login = Column('is_guest_login', Float)
    count = Column('count', Float)
    srv_count = Column('srv_count', Float)
    serror_rate = Column('serror_rate', Float)
    srv_serror_rate = Column('srv_serror_rate', Float)
    rerror_rate = Column('rerror_rate', Float)
    srv_rerror_rate = Column('srv_rerror_rate', Float)
    same_srv_rate = Column('same_srv_rate', Float)
    diff_srv_rate = Column('diff_srv_rate', Float)
    srv_diff_host_rate = Column('srv_diff_host_rate', Float)
    dst_host_count = Column('dst_host_count', Float)
    dst_host_srv_count = Column('dst_host_srv_count', Float)
    dst_host_same_srv_rate = Column('dst_host_same_srv_rate', Float)
    dst_host_diff_srv_rate = Column('dst_host_diff_srv_rate', Float)
    dst_host_same_src_port_rate = Column('dst_host_same_src_port_rate', Float)
    dst_host_srv_diff_host_rate = Column('dst_host_srv_diff_host_rate', Float)
    dst_host_serror_rate = Column('dst_host_serror_rate', Float)
    dst_host_srv_serror_rate = Column('dst_host_srv_serror_rate', Float)
    dst_host_rerror_rate = Column('dst_host_rerror_rate', Float)
    dst_host_srv_rerror_rate = Column('dst_host_srv_rerror_rate', Float)
    attack_type = Column('attack_type', Integer)