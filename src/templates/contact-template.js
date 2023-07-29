import React from "react";
import Layout from "../components/layout";
import { graphql } from "gatsby";
import styled from "styled-components";

const ContactTemplate = ({ data }) => {
  const { html, frontmatter } = data.markdownRemark;

  return (
    <Layout title={frontmatter.title}>
      <ContactWrapper>
        <ContactCopy dangerouslySetInnerHTML={{ __html: html }} />
      </ContactWrapper>
    </Layout>
  );
};

export default ContactTemplate;

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