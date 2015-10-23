Title: System Containers and App Containers
Date: 2015-09-28 12:05
Tags: containers, juju, planet
Slug: 2015-system-containers-and-app-containers
Category: devops
Status: draft
Image: /images/2015/sept/system-and-app-containers.png

Thanks to Docker, application containers have gained significant popularity among
Developer and Ops communities alike. Many people simply want to use Docker
because of its rising popularity, but without understanding if an application
container is what they need. There are many container technologies out there to
choose from, but there is a general lack of knowledge about the subtle
differences in these technologies and when to use what.

## Common cases where containers are used

A majority of call container use cases fall into one of two categories: as a
usual operating system, or as an application packaging mechanism. There are
other use cases like [using containers as routers](http://www.flockport.com/flockport-labs-use-lxc-containers-as-routers/)
but I don't want to get into those at the moment.

Classifying the containers into special types based on how they can be used is
beneficial to how you approach the comprehension of container technology. I will
also point out that it is not a must to use container tech just for these cases.
There are many other use cases, and thats perfectly acceptable.

### OS Containers

OS Containers are virtual environments that share the kernel of the host OS but
provide user space isolation. You can almost think of OS containers as VM's. There
are some differences here, such as no Hypervisor + dedicated isolated resources.
You can install, configure, and run different applications, libraries etc., just
as you would on any OS. Anything running inside a container can only see resources
that are assigned to that container.

#### Built from debootstrapped FS images

You can build an OS container image from just about any debootstrapped filesystem
tree. These miniamlist templates lend themselves to being familiar to anyone who
has done their own distribution work.

#### Full system virtualization

OS Containers ship with init, cron, and the other niceties you would expect from
a traditional linux system. Some applications and libraries may make use of these
utilities to do things like regenerate cache, send reports, ensure the application
is up and running.

#### Composeable Systems

If you've spent any time automating your infrastructure with configuration management
tools like Chef, Puppet, Salt - you can continue to provision your containers with
these technologies. OS containers act just like a VM. You launch a freshly created
cloud image, and can customize to your hearts content. Continually evolving the
system through inflected change. Bringing your experience in your current tooling
with you.

#### Use cases for OS Containers

OS containers are useful when you want to run a fleet of identical or different
flavors of distros. Most of the time containers are created from templates or
images that dteremine the structure and contents of the container. Thus you
are allowed to create containers that have identical environments with the same
package versions and configurations across all containers, in a hyper dense
fashion that is familiar to you.



### Application Containers

While OS containers are designed to run multiple processes and services,
application containers are designed to package and run a single service.
Container technologies like Docker and Rocket are examples of application
containers. So even though they share the same kernel of the host there are
subtle differences that make them different. For the illustrations I'll use
Docker as our example.


#### Run a single service as a container

When a docker container is launched, it [runs a single process](https://docs.docker.com/reference/run/).
This process is usually the one that runs your application when you create
containers per application. This is very different from the traditional OS
container where you have multiple services running on the same OS.

#### Layers of Containers

![Docker Container Layers]()

Docker containers are built from filesystem layers. Therefore any `RUN` commands
you specify in the [Dockerfile](https://docs.docker.com/reference/builder/) creates
a new [layer](https://docs.docker.com/terms/layer/) for the container. In the
end when you run your container, Docker combines these layers and runs your
container. Layering helps Docker to reduce duplication and increases the re-use
of your layers. This is very helpful when you want to create different containers
for your components from a common ancestor base. You can start with a base
image that is common for all your components and then just add layers which are
specific to your component. Layering also helps when you wish to roll back changes
you can simply switch to the older layers. This eliminates friction in a blue/green
deployment scenario so long as your prior layer has not been garbage collected.

#### Built on OS container Tech

Until 2014, Docker was built on top of LXC (OS Containers), and was a complimentary
developer tool for creating containers. Looking at the [Docker FAQ](https://docs.docker.com/faq/)
they mention a number of points where the two now differ.


#### Use cases for Application Containers

The idea behind application containers is that you create different containers
for each component in your application. This approach works quite well when you
are deploying a distributed, multi-component system using a microservices architecture.
The end state of this model is a system that has different applications and 
services talking to each other using API's and protocols that each service supports.

#### 3-tier architecture in the simplest sense


