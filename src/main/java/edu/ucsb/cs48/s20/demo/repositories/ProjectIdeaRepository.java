package edu.ucsb.cs48.s20.demo.repositories;

import java.util.List;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import edu.ucsb.cs48.s20.demo.entities.ProjectIdea;
import edu.ucsb.cs48.s20.demo.entities.Student;

@Repository
public interface ProjectIdeaRepository extends CrudRepository<ProjectIdea, Long> {
  List<ProjectIdea> findByStudent(Student student);
}