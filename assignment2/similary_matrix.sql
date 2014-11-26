select sum (d.count * dt.count) as count
from frequency d, frequency dt
where d.term = dt.term
and d.docid < dt.docid
and d.docid = '10080_txt_crude'
and dt.docid = '17035_txt_earn'
group by d.docid, dt.docid;
