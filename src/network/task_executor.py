import_threading  class_TaskExecutor: def___init__(self): self.tasks_=_[]  def_add_task(self,_function,_args=()): """Add_a_task_to_the_execution_queue.""" task_=_threading.Thread(target=function,_args=args) self.tasks.append(task)  def_run_all(self): """Execute_all_tasks_in_parallel.""" for_task_in_self.tasks: task.start() for_task_in_self.tasks: task.join() print("All_tasks_completed.")  Example_usage if___name___==_"__main__": def_sample_task(name): print(f"Task_{name}_is_running.")  executor_=_TaskExecutor() executor.add_task(sample_task,_args=("A",)) executor.add_task(sample_task,_args=("B",)) executor.run_all()