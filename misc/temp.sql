DROP TABLE widgets;

CREATE TABLE widgets(
        "pid" INT PRIMARY KEY autoincrement,
        "name" CHAR(64) NOT NULL,
        "partCount" int NOT NULL,
        "created" timestamp DEFAULT CURRENT_TIMESTAMP,
        "modified" timestamp NULL
);


CREATE TRIGGER update_widgets_Trigger
AFTER UPDATE On widgets
BEGIN
   UPDATE widgets SET modified = CURRENT_TIMESTAMP WHERE pid = NEW.pid;
END;

INSERT INTO widgets (pid, name, partCount) VALUES (1, 'test', 20);
UPDATE widgets SET partCount = 5 WHERE pid = 1;
