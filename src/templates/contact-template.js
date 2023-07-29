import React from "react";
import { graphql } from "gatsby";
import Layout from "../components/layout";
import {
  NetlifyForm,
  Honeypot,
} from "react-netlify-forms";
import styled from "styled-components";

const ContactTemplate = ({ data }) => {
  const { html, frontmatter } = data.markdownRemark;

  return (
    <Layout title={frontmatter.title}>
      <ContactWrapper>
        <ContactCopy dangerouslySetInnerHTML={{ __html: html }} />
        <ContactForm />
      </ContactWrapper>
    </Layout>
  );
};

export default ContactTemplate;

const ContactForm = () => (
  <NetlifyForm name='Contact' action='/thanks' honeypotName='bot-field'>
    {({ handleChange, success, error }) => (
      <>
        <Honeypot /> 
        {success && <p>Thanks for contacting us!</p>}
        {error && (
          <p>Sorry, we could not reach our servers. Please try again later.</p>
        )}
        <div>
          <label htmlFor='name'>Name:</label>
          <input type='text' name='name' id='name' onChange={handleChange} />
        </div>
        <div>
          <label htmlFor='message'>Message:</label>
          <textarea
            type='text'
            name='message'
            id='message'
            rows='4'
            onChange={handleChange}
          />
        </div>
        <div>
          <button type='submit'>Submit</button>
        </div>
      </>
    )}
  </NetlifyForm>
)

const ContactWrapper = styled.div`
  display: flex;
  align-items: center;
  height: 100%;
  justify-content: space-around;
  margin-top: 1rem;
  padding-bottom: 1rem;

  & > * {
    flex: 1;
  }

  @media screen and (max-width: 1000px) {
    & {
      flex-direction: column;
      justify-content: flex-start;
    }

    & > * {
      margin-top: 2rem;
      flex: 0;
      width: 100%;
    }
  }
`;

const ContactCopy = styled.div`
  max-width: 45ch;

  & p {
    font-size: var(--size-400);
  }

  & a {
    color: #f43f5e;
  }
`;

const FormWrapper = styled.div`
  max-width: 45ch;
  padding: 1rem;
  padding-top: 0;
  border-radius: 4px;
  border: 1px solid rgba(255, 255, 255, 0.7);
  background-color: rgba(255, 255, 255, 0.5);
  backdrop-filter: blur(10px);

  body.dark-mode & {
    background-color: #3b3b3c;
    border: 1px solid #515151;
  }
`;

const FormGroup = styled.div`
  display: flex;
  flex-direction: column;
  font-family: inherit;

  & label {
    margin-top: 1rem;
    text-transform: capitalize;
    font-size: var(--size-400);
  }

  & input,
  textarea {
    resize: vertical;
    font-size: var(--size-400);
    font-family: inherit;
    padding: 0.25rem 0.5rem;
    border-radius: 4px;
    background-color: #fecdd3;
    border: 1px solid #fda4af;
  }

  body.dark-mode & input,
  body.dark-mode & textarea {
    background-color: #4f4f50;
    border: 1px solid #89898a;
  }

  & textarea:focus,
  input:focus {
    outline: none;
    border: 1px solid #665b5c;
  }
`;

const FormErrorMessage = styled.span`
  color: red;
  font-size: var(--size-300);
  opacity: 0.7;
`;

const FormFeedbackWrapper = styled.div`
  margin-top: 1rem;
  text-transform: uppercase;
  font-size: var(--size-300);
`;

const FormSuccessFeedback = styled.span`
  color: green;
`;

const FormErrorFeedback = styled.span`
  color: red;
`;

const FormButton = styled.button`
  margin-top: 1rem;
  padding: 0.45rem;
  padding-left: 1.25rem;
  padding-right: 1.5rem;
  background-color: #f43f5e;
  color: #fafafa;
  border: none;
  text-transform: uppercase;
  border-radius: 4px;
`;

export const pageQuery = graphql`
  query($slug: String!) {
    markdownRemark(fields: { slug: { eq: $slug } }) {
      html
      frontmatter {
        title
      }
    }
  }
`;
