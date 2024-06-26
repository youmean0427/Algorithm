SELECT COUNT(ID) AS COUNT
FROM ECOLI_DATA
WHERE SUBSTR(BIN(GENOTYPE >> 1), LENGTH(BIN(GENOTYPE >> 1))) = 0
AND (SUBSTR(BIN(GENOTYPE), LENGTH(BIN(GENOTYPE))) = 1 OR 
     SUBSTR(BIN(GENOTYPE >> 2), LENGTH(BIN(GENOTYPE >> 2))) = 1)