-- Список курсів, які певному студенту читає певний викладач.
SELECT students.fullname, teachers.fullname, disciplines.name
FROM grades
         LEFT JOIN students ON students.id = grades.student_id
         LEFT JOIN disciplines ON disciplines.id = grades.discipline_id
         LEFT JOIN teachers ON teachers.id = disciplines.teacher_id
WHERE grades.student_id = 3
  AND teachers.id = 4
GROUP BY disciplines.name;