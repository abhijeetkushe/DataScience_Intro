select max(count) from  (select sum (d.count * dt.count) as count
from corpus d, corpus dt
where d.term = dt.term
and d.docid < dt.docid
and dt.docid = 'q'
group by d.docid, dt.docid);

create view corpus as SELECT * FROM frequency
UNION
SELECT 'q' as docid, 'washington' as term, 1 as count 
UNION
SELECT 'q' as docid, 'taxes' as term, 1 as count
UNION 
SELECT 'q' as docid, 'treasury' as term, 1 as count