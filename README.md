# SOLID Principles

Project about learning the five Principles of the SOLID 


### S - Single Responsability Principle
#### *Every software component should have one and only one responsibility*
#### [Live code example](https://github.com/antonio-dias/solid-principles/tree/master/1%20-%20Single%20Responsability%20Principle/live_example)

> ### Cohesion
> Cohesion is the degree to which the various parts of a software component are related
> 
> Higher cohesion helps attain better adherence to the Single Responsability Principle
>> [example](https://github.com/antonio-dias/solid-principles/tree/master/1%20-%20Single%20Responsability%20Principle/cohesion) 
>
> ### Coupling
> Coupling is defined as the level of inter dependency between various software components
> 
> Loose Coupling helps attain better adherence to the Single Responsability Principle
>> [example](https://github.com/antonio-dias/solid-principles/tree/master/1%20-%20Single%20Responsability%20Principle/coupling)

### O - Open Closed Principle
#### *Software components should be closed for modification, but open for extension*
#### [Live code example](https://github.com/antonio-dias/solid-principles/tree/master/2%20-%20Open%20Closed%20Principle/live_example)

> ### Key Takeaways
> Ease of adding new features.
> 
> Leads to minimal cost of developing and testing software.
> 
> Open Closed principal often requires decoupling, which, in turn, automatically follows the Single Responsability Principal.
>
> ### Caution
> 
> Do not follow the Open Closed Principle blindly.
> 
> You will end up with a huge number of classes that can complicate your overall design.
> 
> Make a subjective, rather than an objective decision.
 
### L - Liskov Substitution Principle
#### *Objects should be replaceable with their subtypes without affecting the correctness of the program*
#### [Live code example](https://github.com/antonio-dias/solid-principles/tree/master/3%20-%20Liskov%20Substitution%20Principle/live_example)

> ### Solution patterns
> Break the hierarchy
> 
> "Tell, don't ask"