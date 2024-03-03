-- Create Table & Insert Rows
DROP TABLE IF EXISTS `osk-demo-277900.osk.sample`;

CREATE TABLE `osk-demo-277900.osk.sample`
(
    id int64,
    label string,
    value string
)
;

INSERT INTO `osk-demo-277900.osk.sample`
VALUES
(1, 'name', 'oscar'),
(2, 'name', 'mona lisa')
;


-- Create Table and load file via Console
DROP TABLE IF EXISTS `osk-demo-277900.osk.profiles`;
CREATE TABLE `osk-demo-277900.osk.profiles`
(
    name string,
    marital_status string,
    age int64,
    income int64
)
;