# Smarterhome

[![Build Status](https://travis-ci.com/Kimbahir/Smarterhome.svg?branch=master)](https://travis-ci.com/Kimbahir/Smarterhome)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

Smarterhome is a python wrapper for Tados API for their smart thermostats

## Table of contents

* [Background](#background)
* [Getting started](#getting-started)
  * [Download](#download)
  * [Usage](#usage)
* [Learning tasks](#learning-tasks)
* [Inspiration](#inspiration)

## Background

The project is focused on using the Tado smart thermostats
for establishing whether the home is empty or not, for
leveraging the geofencing to other tools and devices.

Currently there are also aspects of using the data feed
for other data analysis, as the weather and air quality data
looks intriguing :)

## Getting started

Currently it is just a class with methods you can call, but
expect there to be a container that can be initialized and
act as a stand-alone proxy between you and your Tado

### Download

Download the directory TadoToolkit and let the TadoToolkit
be part of your Python project

### Usage

Call the methods now. Please beware that it expects two
environment variables to be present:

* TADO_PASS="password here"
* TADO_EMAIL="email here"

## Learning tasks

So fair I have additional things I want to get out of this
project. In no particular order:

1. Make sure that pytest is used from the get-go
1. Use Code coverage to ensure testing is done proficiently
1. Let documentation be done properly
1. Use a class construct to facilitate easier use of say APIs
and other interesting interactions
1. Use Githubs way of storing keys outside of the repo for safe
access

## Inspiration

Right now my primary sources of input on interacting with
my TADO is from these links:

* <https://shkspr.mobi/blog/2019/02/tado-api-guide-updated-for-2019/>
* <https://github.com/teabot/tado-metrics>
